"""StepFun provider profile."""

from providers.base import ProviderProfile
from providers import register_provider

stepfun = ProviderProfile(
    name="stepfun",
    aliases=("step", "stepfun-coding-plan"),
    env_vars=("STEPFUN_API_KEY",),
    base_url="https://api.stepfun.ai/step_plan/v1",
)

register_provider(stepfun)
