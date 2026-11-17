import os

from dotenv import load_dotenv

load_dotenv(override=True)

# Environment variables for all providers
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/openai/gpt-4o-mini")

LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1")
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "nvidia/nemotron-3-nano-4b")
LM_STUDIO_API_KEY = os.getenv("LM_STUDIO_API_KEY", "lm-studio")

# Active provider selector (defined here, not in .env)
LLM_PROVIDER = "lm_studio"  # "openrouter" or "lm_studio"

# Shared LLM settings
LLM_TEMPERATURE = 0.6
LLM_TIMEOUT = 120  # seconds
