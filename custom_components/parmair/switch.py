"""Switch platform for Parmair MAC integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    REG_HEATER_ENABLE,
    REG_SUMMER_MODE,
    REG_TIME_PROGRAM_ENABLE,
)
from .coordinator import ParmairCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Parmair switch platform."""
    coordinator: ParmairCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[SwitchEntity] = [
        ParmairSwitch(
            coordinator,
            entry,
            REG_SUMMER_MODE,
            "Summer Mode",
            "mdi:weather-sunny",
            "Enables heat recovery summer operation mode",
        ),
        ParmairSwitch(
            coordinator,
            entry,
            REG_TIME_PROGRAM_ENABLE,
            "Time Program",
            "mdi:clock-outline",
            "Enables weekly time program control",
        ),
        ParmairSwitch(
            coordinator,
            entry,
            REG_HEATER_ENABLE,
            "Post Heater",
            "mdi:radiator",
            "Enables post-heating element",
        ),
    ]

    async_add_entities(entities)


class ParmairSwitch(CoordinatorEntity[ParmairCoordinator], SwitchEntity):
    """Representation of a Parmair switch."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: ParmairCoordinator,
        entry: ConfigEntry,
        data_key: str,
        name: str,
        icon: str,
        description: str,
    ) -> None:
        """Initialize the switch."""
        super().__init__(coordinator)
        self._data_key = data_key
        self._attr_name = name
        self._attr_icon = icon
        self._attr_unique_id = f"{entry.entry_id}_{data_key}"
        self._attr_device_info = coordinator.device_info
        self._attr_entity_registry_enabled_default = True

    @property
    def is_on(self) -> bool | None:
        """Return true if switch is on."""
        value = self.coordinator.data.get(self._data_key)
        return value == 1 if value is not None else None

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        try:
            await self.coordinator.async_write_register(self._data_key, 1)
            await self.coordinator.async_request_refresh()
        except Exception as ex:
            _LOGGER.error("Failed to turn on %s: %s", self._data_key, ex)
            raise

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        try:
            await self.coordinator.async_write_register(self._data_key, 0)
            await self.coordinator.async_request_refresh()
        except Exception as ex:
            _LOGGER.error("Failed to turn off %s: %s", self._data_key, ex)
            raise
