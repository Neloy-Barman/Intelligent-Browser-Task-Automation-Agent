from crewai import LLM

from config.llm_config import LLM_TEMPERATURE, OPENROUTER_API_KEY, OPENROUTER_MODEL

llm = LLM(
    model=OPENROUTER_MODEL,
    is_litellm=True,
    api_key=OPENROUTER_API_KEY,
    temperature=LLM_TEMPERATURE,
)
