"""Custom types for Swiss Water."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import SwissWaterApiClient
    from .coordinator import SwissWaterDataUpdateCoordinator


type SwissWaterConfigEntry = ConfigEntry[SwissWaterData]


@dataclass
class SwissWaterData:
    """Data for the SwissWater integration."""

    client: SwissWaterApiClient
    coordinator: SwissWaterDataUpdateCoordinator
    integration: Integration
