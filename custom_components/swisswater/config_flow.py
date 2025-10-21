"""Adds config flow for Swiss Water."""

from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from slugify import slugify

from .const import DOMAIN, LOGGER


class SwissWaterFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Swiss Water."""

    VERSION = 1
    MINOR = 1

    async def async_step_user(self, info):
        """Handle a flow initialized by the user."""
        _errors = {}

        if info is not None:
            await self.async_set_unique_id(
                ## Do NOT use this in production code
                ## The unique_id should never be something that can change
                ## https://developers.home-assistant.io/docs/config_entries_config_flow_handler#unique-ids
                unique_id=slugify(info[CONF_STATION])
            )
            self._abort_if_unique_id_configured()

        return self.async_create_entry(
            title=info[CONF_STATION],
            data=info,
        )
