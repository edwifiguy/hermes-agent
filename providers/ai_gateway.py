"""AI Gateway (Vercel) provider profile.

AI Gateway routes to multiple backends. Hermes sends attribution
headers and full reasoning config passthrough.
"""

from typing import Any, Dict, Tuple

from providers.base import ProviderProfile
from providers import register_provider


class AIGatewayProfile(ProviderProfile):
    """Vercel AI Gateway — attribution headers + reasoning passthrough."""

    def build_api_kwargs_extras(
        self, *, reasoning_config: dict = None, supports_reasoning: bool = True, **ctx
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        extra_body: Dict[str, Any] = {}
        if supports_reasoning and reasoning_config is not None:
            extra_body["reasoning"] = dict(reasoning_config)
        elif supports_reasoning:
            extra_body["reasoning"] = {"enabled": True, "effort": "medium"}
        return extra_body, {}


ai_gateway = AIGatewayProfile(
    name="ai-gateway",
    aliases=("vercel-ai-gateway", "ai_gateway"),
    env_vars=("AI_GATEWAY_API_KEY",),
    base_url="https://ai-gateway.vercel.sh/v1",
    default_headers={
        "HTTP-Referer": "https://hermes-agent.nousresearch.com",
        "X-Title": "Hermes Agent",
    },
)

register_provider(ai_gateway)
