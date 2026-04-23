"""Arcee AI provider profile."""

from providers.base import ProviderProfile
from providers import register_provider

arcee = ProviderProfile(
    name="arcee",
    aliases=("arcee-ai", "arceeai"),
    env_vars=("ARCEE_API_KEY",),
    base_url="https://api.arcee.ai/api/v1",
)

register_provider(arcee)
