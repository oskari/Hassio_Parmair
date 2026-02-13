"""Tests for Parmair data interpretation using fixture dumps.

These tests validate that the integration correctly interprets register values
from Parmair devices. Tests are parametrized to run against all available
fixture files, ensuring compatibility with different machine types.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pytest

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "tools"))

from tools.mock_coordinator import MockCoordinator


class TestFixtureLoading:
    """Test that fixture files load correctly."""

    def test_fixture_loads_successfully(self, coordinator: MockCoordinator) -> None:
        """Verify fixture file loads without errors."""
        assert coordinator is not None
        assert coordinator.data is not None
        assert len(coordinator.data) > 0

    def test_fixture_has_metadata(self, fixture_metadata: dict[str, Any]) -> None:
        """Verify fixture has required metadata."""
        assert "register_map_version" in fixture_metadata or "detected_software_version" in fixture_metadata
        
    def test_fixture_has_registers(self, fixture_registers: dict[str, Any]) -> None:
        """Verify fixture has register data."""
        assert len(fixture_registers) > 0


class TestSystemInfo:
    """Test system information interpretation."""

    def test_software_version_present(self, coordinator: MockCoordinator) -> None:
        """Software version should be present and valid."""
        sw_ver = coordinator.data.get("software_version")
        assert sw_ver is not None, "Software version should be present"
        assert isinstance(sw_ver, (int, float)), "Software version should be numeric"
        assert 0.5 <= sw_ver <= 10.0, f"Software version {sw_ver} out of expected range"

    def test_hardware_type_present(self, coordinator: MockCoordinator) -> None:
        """Hardware type should be present and valid."""
        hw_type = coordinator.data.get("hardware_type")
        assert hw_type is not None, "Hardware type should be present"
        # Valid MAC models: 80, 100, 120, 150, etc.
        assert 50 <= hw_type <= 500, f"Hardware type {hw_type} out of expected range"

    def test_device_info_valid(self, coordinator: MockCoordinator) -> None:
        """Device info should have required fields."""
        device_info = coordinator.device_info
        assert "name" in device_info
        assert "manufacturer" in device_info
        assert device_info["manufacturer"] == "Parmair"
        assert "model" in device_info
        assert "MAC" in device_info["model"]


class TestTemperatures:
    """Test temperature interpretation."""

    TEMP_KEYS = [
        "fresh_air_temp",
        "supply_after_recovery_temp",
        "supply_temp",
        "exhaust_temp",
        "waste_temp",
    ]

    SETPOINT_KEYS = [
        "exhaust_temp_setpoint",
        "supply_temp_setpoint",
    ]

    def test_temperatures_present(self, coordinator: MockCoordinator) -> None:
        """At least some temperature values should be present."""
        present = [key for key in self.TEMP_KEYS if key in coordinator.data]
        assert len(present) >= 3, f"Expected at least 3 temperatures, found: {present}"

    @pytest.mark.parametrize("temp_key", TEMP_KEYS)
    def test_temperature_in_valid_range(
        self, coordinator: MockCoordinator, temp_key: str
    ) -> None:
        """Temperature values should be in a physically reasonable range."""
        if temp_key not in coordinator.data:
            pytest.skip(f"{temp_key} not present in fixture")
        
        value = coordinator.data[temp_key]
        assert value is not None
        # Allow -50°C to +80°C range for ventilation systems
        assert -50 <= value <= 80, f"{temp_key}={value}°C out of valid range"

    @pytest.mark.parametrize("setpoint_key", SETPOINT_KEYS)
    def test_setpoint_in_valid_range(
        self, coordinator: MockCoordinator, setpoint_key: str
    ) -> None:
        """Temperature setpoints should be in a reasonable range."""
        if setpoint_key not in coordinator.data:
            pytest.skip(f"{setpoint_key} not present in fixture")
        
        value = coordinator.data[setpoint_key]
        assert value is not None
        # Setpoints typically 10°C to 30°C
        assert 5 <= value <= 35, f"{setpoint_key}={value}°C out of valid range"


class TestStates:
    """Test state interpretation."""

    def test_power_state_valid(self, coordinator: MockCoordinator) -> None:
        """Power state should be a valid value."""
        power = coordinator.data.get("power")
        if power is None:
            pytest.skip("Power state not present")
        
        # V1: 0=Off, 1=Shutting Down, 2=Starting, 3=Running
        # V2: 0=Off, 1=On
        assert power in (0, 1, 2, 3), f"Invalid power state: {power}"

    def test_control_state_valid(self, coordinator: MockCoordinator) -> None:
        """Control state should be a valid value."""
        control = coordinator.data.get("control_state")
        if control is None:
            pytest.skip("Control state not present")
        
        # V1: 0=Stop, 1=Away, 2=Home, 3=Boost, 4=Overpressure, 5-8=Timers, 9=Manual
        # V2: 0=Off, 1=Away, 2=Home, 3=Boost, 4=Sauna, 5=Fireplace
        assert 0 <= control <= 10, f"Invalid control state: {control}"

    def test_defrost_state_binary(self, coordinator: MockCoordinator) -> None:
        """Defrost state should be binary (0 or 1)."""
        defrost = coordinator.data.get("defrost_state")
        if defrost is None:
            pytest.skip("Defrost state not present")
        
        assert defrost in (0, 1), f"Invalid defrost state: {defrost}"


class TestSpeeds:
    """Test speed-related values."""

    def test_actual_speed_valid(self, coordinator: MockCoordinator) -> None:
        """Actual speed should be in valid range."""
        speed = coordinator.data.get("actual_speed")
        if speed is None:
            pytest.skip("Actual speed not present")
        
        # Speed typically 0-5 or similar
        assert 0 <= speed <= 10, f"Invalid actual speed: {speed}"

    def test_fan_speeds_percentage(self, coordinator: MockCoordinator) -> None:
        """Fan speeds should be valid percentages."""
        for key in ("supply_fan_speed", "exhaust_fan_speed"):
            value = coordinator.data.get(key)
            if value is None:
                continue
            
            assert 0 <= value <= 100, f"{key}={value}% out of valid range"

    def test_preset_speeds_valid(self, coordinator: MockCoordinator) -> None:
        """Preset speed settings should be valid."""
        for key in ("home_speed", "away_speed", "boost_setting"):
            value = coordinator.data.get(key)
            if value is None:
                continue
            
            # Preset speeds typically 1-5
            assert 0 <= value <= 10, f"{key}={value} out of valid range"


class TestOptionalSensors:
    """Test optional sensor interpretation."""

    def test_humidity_valid_if_present(self, coordinator: MockCoordinator) -> None:
        """Humidity should be 0-100% if present and installed."""
        humidity = coordinator.data.get("humidity")
        raw = coordinator.get_raw_value("humidity")
        
        if humidity is None or raw in (0, -1, 65535):
            pytest.skip("Humidity sensor not installed")
        
        assert 0 <= humidity <= 100, f"Invalid humidity: {humidity}%"

    def test_co2_valid_if_present(self, coordinator: MockCoordinator) -> None:
        """CO2 should be reasonable ppm if present and installed."""
        co2 = coordinator.data.get("co2")
        raw = coordinator.get_raw_value("co2")
        
        if co2 is None or raw in (0, -1, 65535):
            pytest.skip("CO2 sensor not installed")
        
        # CO2 typically 400-5000 ppm in ventilation scenarios
        assert 200 <= co2 <= 10000, f"Invalid CO2: {co2} ppm"


class TestFilterInfo:
    """Test filter information interpretation."""

    def test_filter_state_valid(self, coordinator: MockCoordinator) -> None:
        """Filter state should be valid."""
        state = coordinator.data.get("filter_state")
        if state is None:
            pytest.skip("Filter state not present")
        
        # V1: 0=Replace, 1=OK
        # V2: 0=OK, 1=Ack, 2=Reminder
        assert state in (0, 1, 2), f"Invalid filter state: {state}"

    def test_filter_date_valid(self, coordinator: MockCoordinator) -> None:
        """Filter date components should be valid."""
        day = coordinator.data.get("filter_day")
        month = coordinator.data.get("filter_month")
        year = coordinator.data.get("filter_year")
        
        if day is None or month is None or year is None:
            pytest.skip("Filter date not present")
        
        assert 1 <= day <= 31, f"Invalid filter day: {day}"
        assert 1 <= month <= 12, f"Invalid filter month: {month}"
        assert 2000 <= year <= 3000, f"Invalid filter year: {year}"

    def test_filter_interval_valid(self, coordinator: MockCoordinator) -> None:
        """Filter interval should be valid."""
        interval = coordinator.data.get("filter_interval")
        if interval is None:
            pytest.skip("Filter interval not present")
        
        # V2: 0=3 months, 1=4 months, 2=6 months
        assert 0 <= interval <= 10, f"Invalid filter interval: {interval}"


class TestPerformance:
    """Test performance metrics interpretation."""

    def test_heat_recovery_efficiency_valid(self, coordinator: MockCoordinator) -> None:
        """Heat recovery efficiency should be 0-100%."""
        efficiency = coordinator.data.get("heat_recovery_efficiency")
        if efficiency is None:
            pytest.skip("Heat recovery efficiency not present")
        
        assert 0 <= efficiency <= 100, f"Invalid efficiency: {efficiency}%"

    def test_heater_outputs_percentage(self, coordinator: MockCoordinator) -> None:
        """Heater outputs should be valid percentages."""
        for key in ("post_heater_output", "pre_heater_output", "heat_recovery_output"):
            value = coordinator.data.get(key)
            if value is None:
                continue
            
            assert 0 <= value <= 100, f"{key}={value}% out of valid range"


class TestScaling:
    """Test that register scaling is applied correctly."""

    def test_temperature_scaling(self, coordinator: MockCoordinator) -> None:
        """Temperature values should be scaled by 0.1."""
        # Check that raw/scaled relationship is correct for a temp register
        raw = coordinator.get_raw_value("supply_temp")
        scaled = coordinator.data.get("supply_temp")
        
        if raw is None or scaled is None:
            pytest.skip("Supply temp not present")
        
        # With 0.1 scaling, raw 174 should give 17.4
        expected = raw * 0.1
        assert abs(scaled - expected) < 0.01, f"Scaling error: raw={raw}, scaled={scaled}, expected={expected}"

    def test_version_scaling(self, coordinator: MockCoordinator) -> None:
        """Version values should be scaled by 0.01."""
        raw = coordinator.get_raw_value("software_version")
        scaled = coordinator.data.get("software_version")
        
        if raw is None or scaled is None:
            pytest.skip("Software version not present")
        
        # With 0.01 scaling, raw 225 should give 2.25
        expected = raw * 0.01
        assert abs(scaled - expected) < 0.001, f"Scaling error: raw={raw}, scaled={scaled}, expected={expected}"


class TestRegisterDefinitions:
    """Test register definition retrieval."""

    def test_get_register_definition(self, coordinator: MockCoordinator) -> None:
        """Register definitions should be retrievable."""
        for key in ("software_version", "power", "fresh_air_temp"):
            if key not in coordinator.data:
                continue
            
            definition = coordinator.get_register_definition(key)
            assert definition is not None
            assert definition.key == key
            assert definition.address > 0

    def test_register_definition_has_label(self, coordinator: MockCoordinator) -> None:
        """Register definitions should have Modbus labels."""
        definition = coordinator.get_register_definition("software_version")
        assert definition.label is not None
        assert len(definition.label) > 0


class TestV2Specific:
    """Tests specific to V2.x firmware."""

    def test_season_state_v2(
        self, coordinator: MockCoordinator, is_v2_device: bool
    ) -> None:
        """V2 devices should have season state."""
        if not is_v2_device:
            pytest.skip("Not a V2 device")
        
        season = coordinator.data.get("season_state")
        if season is None:
            pytest.skip("Season state not present")
        
        # V2: 0=Winter, 1=Transition, 2=Summer
        assert season in (0, 1, 2), f"Invalid V2 season state: {season}"

    def test_hardware_type_mapping_v2(
        self, coordinator: MockCoordinator, is_v2_device: bool
    ) -> None:
        """V2 hardware type codes should map correctly."""
        if not is_v2_device:
            pytest.skip("Not a V2 device")
        
        hw_type = coordinator.data.get("hardware_type")
        if hw_type is None:
            pytest.skip("Hardware type not present")
        
        device_info = coordinator.device_info
        assert "MAC" in device_info["model"]

