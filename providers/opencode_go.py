"""OpenCode Go provider profile (chat_completions subset).

Note: OpenCode Go uses per-model api_mode routing:
  - MiniMax models → anthropic_messages
  - GLM / Kimi models → chat_completions (this profile)
"""

from providers.base import ProviderProfile
from providers import register_provider

opencode_go = ProviderProfile(
    name="opencode-go",
    aliases=("opencode_go",),
    env_vars=("OPENCODE_GO_API_KEY",),
    base_url="https://opencode.ai/zen/go/v1",
)

register_provider(opencode_go)
