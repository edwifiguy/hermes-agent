"""OpenCode Zen provider profile (chat_completions subset).

Note: OpenCode Zen uses per-model api_mode routing:
  - Claude models → anthropic_messages
  - GPT-5/Codex models → codex_responses
  - Everything else → chat_completions (this profile)

This profile covers only the chat_completions portion.
"""

from providers.base import ProviderProfile
from providers import register_provider

opencode_zen = ProviderProfile(
    name="opencode-zen",
    aliases=("opencode_zen",),
    env_vars=("OPENCODE_ZEN_API_KEY",),
    base_url="https://opencode.ai/zen/v1",
)

register_provider(opencode_zen)
