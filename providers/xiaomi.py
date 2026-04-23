"""Xiaomi MiMo provider profile."""

from providers.base import ProviderProfile
from providers import register_provider

xiaomi = ProviderProfile(
    name="xiaomi",
    aliases=("mimo", "xiaomi-mimo"),
    env_vars=("XIAOMI_API_KEY",),
    base_url="https://api.xiaomimimo.com/v1",
)

register_provider(xiaomi)
