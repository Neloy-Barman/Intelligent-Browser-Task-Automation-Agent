from config.llm_config import LLM_PROVIDER

if LLM_PROVIDER == "openrouter":
    from llm_providers.openrouter import llm
else:
    from llm_providers.lm_studio import llm

# __all__ declares the public names exported when someone does
# `from llm_providers.llm_provider import *`. It keeps the module's
# public API limited to `llm`, so importing `*` won't leak other names.
__all__ = ["llm"]
