"""Kilo Code provider profile."""

from providers.base import ProviderProfile
from providers import register_provider

kilocode = ProviderProfile(
    name="kilocode",
    aliases=("kilo-code", "kilo"),
    env_vars=("KILOCODE_API_KEY",),
    base_url="https://api.kilo.ai/api/gateway",
)

register_provider(kilocode)
