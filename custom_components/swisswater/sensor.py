"""Sensor platform for Swiss Water."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.sensor import (SensorEntity,
                                             SensorEntityDescription)

from .entity import SwissWaterEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import SwissWaterDataUpdateCoordinator
    from .data import SwissWaterConfigEntry

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="swisswater",
        name="Swiss Water",
        icon="mdi:format-quote-close",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: SwissWaterConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities(
        SwissWaterSensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class SwissWaterSensor(SwissWaterEntity, SensorEntity):
    """SwissWater Sensor class."""

    def __init__(
        self,
        coordinator: SwissWaterDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str | None:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")
