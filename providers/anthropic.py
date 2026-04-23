"""Native Anthropic provider profile."""

from providers.base import ProviderProfile
from providers import register_provider

anthropic = ProviderProfile(
    name="anthropic",
    aliases=("claude", "claude-oauth"),
    api_mode="anthropic_messages",
    env_vars=("ANTHROPIC_API_KEY", "ANTHROPIC_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN"),
    base_url="https://api.anthropic.com",
    auth_type="api_key",
)

register_provider(anthropic)
