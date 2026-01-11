"""Select platform for Parmair MAC integration."""
from __future__ import annotations

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import ParmairCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Parmair select platform."""
    coordinator: ParmairCoordinator = hass.data[DOMAIN][entry.entry_id]  # noqa: F841

    # No select entities currently configured
    # Example: entities.append(ParmairSelect(coordinator, ...))
    entities: list[SelectEntity] = []

    async_add_entities(entities)
