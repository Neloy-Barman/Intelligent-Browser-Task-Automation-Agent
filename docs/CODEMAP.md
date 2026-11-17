# Code Map

## Environment setup
- `requirements.txt` — Python dependencies (crewai[tools], crewai[litellm], crewai-tools[mcp]).
- `venv/` — Local Python 3.11 virtual environment with the above dependencies installed.

## Notes
- Application source code lives under `agents/`.

## Application
- `agents/browser_automation_agent.py` — Initializes a CrewAI `Agent` (variable `browser_automation_agent`) with `role`, `goal`, `backstory`, and `llm` (from config).
- `tasks/browser_automation_task.py` — Defines a CrewAI `Task` (variable `browser_automation_task`) with `description`, `expected_output`, assigned to `browser_automation_agent`.
- `config/llm_config.py` — Builds a CrewAI `LLM` (variable `llm`) for OpenRouter, reading `OPENROUTER_MODEL` and `OPENROUTER_API_KEY` from environment.
- `.env.example` — Example environment variables for OpenRouter configuration.
- `crew.py` — Defines a CrewAI `Crew` (variable `crew`) with `browser_automation_agent` and `browser_automation_task`.
- `main.py` — Entry point: reads a browser task from user input and kicks off `crew` with interpolated `{task}`.
- `mcp_config/playwright_mcp.py` — Defines Playwright MCP server config (`playwright_mcp_server`) using `MCPServerStdio`.
- `agents/browser_automation_agent.py` — Builds `agent_mcps` list and passes it to the Agent via `mcps`.
