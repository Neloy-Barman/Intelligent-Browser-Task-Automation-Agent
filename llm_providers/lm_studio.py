from crewai import LLM

from config.llm_config import (
    LLM_TEMPERATURE,
    LLM_TIMEOUT,
    LM_STUDIO_API_KEY,
    LM_STUDIO_BASE_URL,
    LM_STUDIO_MODEL,
)

llm = LLM(
    model=f"openai/{LM_STUDIO_MODEL}",
    base_url=LM_STUDIO_BASE_URL,
    api_key=LM_STUDIO_API_KEY,
    temperature=LLM_TEMPERATURE,
    timeout=LLM_TIMEOUT,
)
