# Code Map

## Environment setup
- `requirements.txt` — Python dependencies (crewai[tools], crewai[litellm], crewai-tools[mcp]).
- `venv/` — Local Python 3.11 virtual environment with the above dependencies installed.

## Notes
- Application source code lives under `agents/`.

## Application
- `agents/browser_automation_agent.py` — Initializes a CrewAI `Agent` (variable `browser_automation_agent`) with `role`, `goal`, `backstory`, and `llm` (from llm_providers).
- `tasks/browser_automation_task.py` — Defines a CrewAI `Task` (variable `browser_automation_task`) with `description`, `expected_output`, assigned to `browser_automation_agent`.
- `config/llm_config.py` — Holds all LLM environment variables and defines `LLM_PROVIDER` selector.
- `config/playwright_config.py` — Playwright MCP settings (browser, headless, timeouts).
- `llm_providers/llm_provider.py` — Common LLM provider: builds `llm` for the selected provider using shared settings.
- `llm_providers/__init__.py` — Re-exports `llm` for use by agents.
- `.env.example` — Example environment variables.
- `crew.py` — Defines a CrewAI `Crew` (variable `crew`) with `browser_automation_agent` and `browser_automation_task`.
- `main.py` — Entry point: reads a browser task, imports phoenix_config for global tracer registration, kicks off `crew`.
- `frontend/app.py` — Streamlit UI (title, task input, Run button); backend wiring pending.
- `mcp_servers/playwright_mcp.py` — Builds Playwright MCP args dynamically via `build_playwright_args()` and defines `playwright_mcp_server`.
- `docker-compose.yml` — Runs Arize Phoenix (UI on 6006, OTLP gRPC on 4317) for tracing/evaluations.
- `requirements.txt` — Includes OpenInference instrumentation (crewai, litellm) and arize-phoenix.
- `config/phoenix_config.py` — Phoenix tracing settings (project name, auto_instrument).
- `tracing/phoenix_tracing.py` — Registers Phoenix tracer using settings from config/phoenix_config.py.

## Docs
- docs/IMAGE_PROMPTS.md � Image generation prompts for diagrams and demo materials.
