"""Custom / Ollama (local) provider profile.

Covers any endpoint registered as provider="custom", including local
Ollama instances. Key quirks:
  - ollama_num_ctx → extra_body.options.num_ctx (local context window)
  - reasoning_config disabled → extra_body.think = False
"""

from typing import Any, Dict, Tuple

from providers.base import ProviderProfile
from providers import register_provider


class CustomProfile(ProviderProfile):
    """Custom/Ollama local provider — think=false and num_ctx support."""

    def build_api_kwargs_extras(
        self, *, reasoning_config: dict = None, ollama_num_ctx: int = None, **ctx
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        extra_body: Dict[str, Any] = {}

        # Ollama context window
        if ollama_num_ctx:
            options = extra_body.get("options", {})
            options["num_ctx"] = ollama_num_ctx
            extra_body["options"] = options

        # Disable thinking when reasoning is turned off
        if reasoning_config and isinstance(reasoning_config, dict):
            _effort = (reasoning_config.get("effort") or "").strip().lower()
            _enabled = reasoning_config.get("enabled", True)
            if _effort == "none" or _enabled is False:
                extra_body["think"] = False

        return extra_body, {}


custom = CustomProfile(
    name="custom",
    aliases=("ollama", "local"),
    env_vars=(),  # No fixed key — custom endpoint
    base_url="",  # User-configured
)

register_provider(custom)
