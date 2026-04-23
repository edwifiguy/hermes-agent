"""xAI (Grok) provider profile."""

from providers.base import ProviderProfile
from providers import register_provider

xai = ProviderProfile(
    name="xai",
    aliases=("grok", "x-ai"),
    api_mode="codex_responses",
    env_vars=("XAI_API_KEY",),
    base_url="https://api.x.ai/v1",
    auth_type="api_key",
)

register_provider(xai)
