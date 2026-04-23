"""AWS Bedrock provider profile."""

from providers.base import ProviderProfile
from providers import register_provider

bedrock = ProviderProfile(
    name="bedrock",
    aliases=("aws", "aws-bedrock", "amazon-bedrock", "amazon"),
    api_mode="bedrock_converse",
    env_vars=(),               # AWS SDK credentials — not env vars
    base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
    auth_type="aws",
)

register_provider(bedrock)
