"""Hugging Face provider profile."""

from providers.base import ProviderProfile
from providers import register_provider

huggingface = ProviderProfile(
    name="huggingface",
    aliases=("hf", "hugging-face"),
    env_vars=("HF_TOKEN",),
    base_url="https://router.huggingface.co/v1",
)

register_provider(huggingface)
