"""Select platform for Parmair MAC integration."""

from __future__ import annotations

import logging

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    _hass: HomeAssistant,
    _entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Parmair select platform."""
    coordinator: ParmairCoordinator = hass.data[DOMAIN][entry.entry_id]
    is_v2 = coordinator.software_version == SOFTWARE_VERSION_2 or str(
        coordinator.software_version
    ).startswith("2.")

    entities: list[SelectEntity] = [
        ParmairFilterIntervalSelect(coordinator, entry),
        ParmairManualSpeedSelect(coordinator, entry),
        ParmairSpeedPresetSelect(coordinator, entry, REG_HOME_SPEED, "Home Speed Preset"),
        ParmairSpeedPresetSelect(coordinator, entry, REG_AWAY_SPEED, "Away Speed Preset"),
        ParmairBoostSpeedSelect(coordinator, entry),
        ParmairBoostDurationSelect(coordinator, entry),
        ParmairOverpressureDurationSelect(coordinator, entry),
    ]
    if is_v2:
        entities.append(ParmairSummerModeSelect(coordinator, entry))

    async_add_entities(entities)
