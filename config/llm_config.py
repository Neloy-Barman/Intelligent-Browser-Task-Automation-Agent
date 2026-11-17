import os

from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/openai/gpt-4o-mini")

llm = LLM(
    model=OPENROUTER_MODEL,
    is_litellm=True,
    api_key=OPENROUTER_API_KEY,
    temperature=0.6,
)
