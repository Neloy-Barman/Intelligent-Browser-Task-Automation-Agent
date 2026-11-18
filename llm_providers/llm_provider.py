from crewai import LLM

from config.llm_config import (
    LLM_API_KEY,
    LLM_BASE_URL,
    LLM_IS_LITELLM,
    LLM_MODEL,
    LLM_TEMPERATURE,
    LLM_TIMEOUT,
)

# Common LLM construction using the shared variables from config/llm_config.py.
kwargs = {
    "model": LLM_MODEL,
    "api_key": LLM_API_KEY,
    "temperature": LLM_TEMPERATURE,
    "timeout": LLM_TIMEOUT,
}
if LLM_BASE_URL:
    kwargs["base_url"] = LLM_BASE_URL
if LLM_IS_LITELLM:
    kwargs["is_litellm"] = True

llm = LLM(**kwargs)

# __all__ declares the public names exported when someone does
# `from llm_providers.llm_provider import *`. It limits the public API to `llm`.
__all__ = ["llm"]
