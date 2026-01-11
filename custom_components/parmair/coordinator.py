"""DataUpdateCoordinator for Parmair integration."""
from __future__ import annotations

import contextlib
import logging
import threading
import time
from datetime import timedelta
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException

from .const import (
    CONF_HEATER_TYPE,
    CONF_SCAN_INTERVAL,
    CONF_SLAVE_ID,
    CONF_SOFTWARE_VERSION,
    DEFAULT_NAME,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    HARDWARE_TYPE_MAP_V2,
    HEATER_TYPE_UNKNOWN,
    POLLING_REGISTER_KEYS,
    SOFTWARE_VERSION_1,
    SOFTWARE_VERSION_2,
    RegisterDefinition,
    get_register_definition,
    get_registers_for_version,
)

_LOGGER = logging.getLogger(__name__)


def _read_registers(client: ModbusTcpClient, address: int, count: int, slave_id: int):
    """Read holding registers with pymodbus 3.7+ compatibility (slave vs device_id)."""
    try:
        return client.read_holding_registers(address=address, count=count, slave=slave_id)  # type: ignore[call-arg]
    except TypeError:
        return client.read_holding_registers(address=address, count=count, device_id=slave_id)


def _write_register(client: ModbusTcpClient, address: int, value: int, slave_id: int):
    """Write register with pymodbus 3.7+ compatibility (slave vs device_id)."""
    try:
        return client.write_register(address, value, slave=slave_id)  # type: ignore[call-arg]
    except TypeError:
        return client.write_register(address, value, device_id=slave_id)


class ParmairCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Class to manage fetching Parmair data from Modbus."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize the coordinator."""
        self.entry = entry
        self.host = entry.data[CONF_HOST]
        self.port = entry.data[CONF_PORT]
        self.slave_id = entry.data[CONF_SLAVE_ID]
        self.software_version = entry.data.get(CONF_SOFTWARE_VERSION, SOFTWARE_VERSION_1)
        self.heater_type = entry.data.get(CONF_HEATER_TYPE, HEATER_TYPE_UNKNOWN)

        scan_interval = entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)

        # Get version-specific register map
        self._registers = get_registers_for_version(self.software_version)

        self._poll_registers: list[RegisterDefinition] = [
            self._registers[key]
            for key in POLLING_REGISTER_KEYS
            if key in self._registers
        ]

        self._client = ModbusTcpClient(host=self.host, port=self.port)
        self._lock = threading.Lock()

        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_{self.host}",
            update_interval=timedelta(seconds=scan_interval),
        )

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from Parmair via Modbus."""
        try:
            result = await self.hass.async_add_executor_job(self._read_modbus_data)
            return dict(result)  # Explicit conversion to satisfy type checker
        except ModbusException as err:
            raise UpdateFailed(f"Error communicating with Parmair device: {err}") from err

    def _read_modbus_data(self) -> dict[str, Any]:
        """Read data from Modbus (runs in executor)."""
        with self._lock:
            # Close and reconnect to flush any stale responses in buffer
            if self._client.connected:
                with contextlib.suppress(Exception):
                    self._client.close()

            if not self._client.connect():
                raise ModbusException("Failed to connect to Modbus device")

            # Small delay after connect to allow device to stabilize
            time.sleep(0.05)

            data: dict[str, Any] = {}
            failed_registers = []

            try:
                for definition in self._poll_registers:
                    value = self._read_register_value(definition)
                    if value is None:
                        failed_registers.append(f"{definition.label}({definition.register_id})")
                        continue
                    data[definition.key] = value
                    # Delay between reads to prevent transaction ID conflicts
                    time.sleep(0.05)

                if failed_registers:
                    _LOGGER.debug(
                        "Failed to read %d registers: %s",
                        len(failed_registers),
                        ", ".join(failed_registers),
                    )

                _LOGGER.debug(
                    "Read data from Parmair %s: %d values - %s",
                    self.host,
                    len(data),
                    data,
                )
                return data

            except Exception as ex:
                _LOGGER.error("Error reading from Modbus: %s", ex)
                raise ModbusException(f"Failed to read data: {ex}") from ex
            finally:
                # Always close after reading to prevent buffer buildup
                with contextlib.suppress(Exception):
                    self._client.close()

    def write_register(self, key: str, value: float | int) -> bool:
        """Write a value to a Modbus register respecting scaling."""

        definition = get_register_definition(key)
        try:
            with self._lock:
                if not self._client.connected and not self._client.connect():
                    return False

                raw_value = self._to_raw(definition, value)
                result = _write_register(self._client, definition.address, raw_value, self.slave_id)
                return not result.isError()
        except Exception as ex:
            _LOGGER.error(
                "Error writing to Modbus register %s (%s): %s",
                definition.register_id,
                definition.label,
                ex,
            )
            return False

    async def async_write_register(self, key: str, value: float | int) -> bool:
        """Write a value to a Modbus register (async)."""
        result = await self.hass.async_add_executor_job(self.write_register, key, value)
        return bool(result)

    async def async_shutdown(self) -> None:
        """Close the Modbus connection."""
        def _close():
            with self._lock:
                if self._client.connected:
                    self._client.close()

        await self.hass.async_add_executor_job(_close)

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        sw_version = self.data.get("software_version")
        hw_type = self.data.get("hardware_type")

        # Determine MAC model from hardware type
        model = "MAC"
        if hw_type is not None:
            hw_type_int = int(hw_type)
            # For V2, use mapping if available, otherwise use raw value
            if self.software_version == SOFTWARE_VERSION_2:
                model_num = HARDWARE_TYPE_MAP_V2.get(hw_type_int, hw_type_int)
            else:
                model_num = hw_type_int
            model = f"MAC {model_num}"

        device_info = DeviceInfo(
            identifiers={(DOMAIN, self.entry.entry_id)},
            name=self.entry.data.get("name", DEFAULT_NAME),
            manufacturer="Parmair",
            model=model,
        )

        # Add software version
        if sw_version is not None:
            if isinstance(sw_version, (int, float)):
                device_info["sw_version"] = f"{sw_version:.2f}"
            else:
                device_info["sw_version"] = str(sw_version)

        return device_info

    def get_register_definition(self, key: str) -> RegisterDefinition:
        """Expose register metadata for other components."""
        return get_register_definition(key, self._registers)

    def _read_register_value(self, definition: RegisterDefinition) -> Any | None:
        """Read and scale a single register."""
        result = _read_registers(self._client, definition.address, 1, self.slave_id)
        if not result or result.isError():
            _LOGGER.warning(
                "Failed reading register %s (%s) at address %d",
                definition.register_id,
                definition.label,
                definition.address,
            )
            return None

        raw = result.registers[0]

        # Convert to signed int16 if value is > 32767 (handle negative temperatures)
        if raw > 32767:
            raw = raw - 65536

        if definition.optional and raw < 0:
            # Device reports -1 when module isn't installed
            return None

        return self._from_raw(definition, raw)

    @staticmethod
    def _from_raw(definition: RegisterDefinition, raw: int) -> float | int:
        """Convert raw register value to engineering units."""

        if definition.scale == 1:
            return raw
        return raw * definition.scale

    @staticmethod
    def _to_raw(definition: RegisterDefinition, value: float | int) -> int:
        """Convert a scaled value back to raw register units."""

        if definition.scale == 1:
            return int(value)
        return int(round(float(value) / definition.scale))
