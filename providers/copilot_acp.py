"""GitHub Copilot ACP provider profile.

copilot-acp uses an external ACP subprocess — NOT the standard
transport. api_mode="copilot_acp" is handled separately in run_agent.py.
The profile captures auth + endpoint metadata for registry migration.
"""

from providers.base import ProviderProfile
from providers import register_provider

copilot_acp = ProviderProfile(
    name="copilot-acp",
    aliases=("github-copilot-acp", "copilot-acp-agent"),
    api_mode="copilot_acp",
    env_vars=(),                       # Managed by ACP subprocess
    base_url="acp://copilot",          # ACP internal scheme
    auth_type="external_process",
)

register_provider(copilot_acp)
