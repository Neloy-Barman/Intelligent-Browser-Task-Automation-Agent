# Plan

## Completed
- [x] Create virtual environment `venv` (Python 3.11.9).
- [x] Create `requirements.txt` with crewai[tools], crewai[litellm], crewai-tools[mcp].
- [x] Install all dependencies into `venv` (verified import of crewai, crewai_tools, litellm).
- [x] Create `agents/` folder with `browser_automation_agent.py` initializing a CrewAI Agent (`browser_automation_agent`) with `role`, `goal`, and `backstory`.
- [x] Create `tasks/` folder with `browser_automation_task.py` defining a CrewAI Task (`browser_automation_task`) with `description`, `expected_output`, assigned to `browser_automation_agent`.
- [x] Create `config/` folder with `llm_config.py` defining an OpenRouter-backed CrewAI `LLM` (`llm`) reading model name and API key from environment.
- [x] Add `.env.example` with OpenRouter environment variable placeholders.
- [x] Wire `llm` into `browser_automation_agent`.
- [x] Create `crew.py` defining a CrewAI `Crew` (`crew`) with the browser automation agent and task.
- [x] Add variable interpolation (`{task}`) to `browser_automation_task` description.
- [x] Create `main.py` entry point that takes user input and kicks off the crew.
- [x] Create `mcp_servers/` folder with `playwright_mcp.py` defining Playwright MCP server config.
- [x] Wire Playwright MCP tools into `browser_automation_agent`.
- [x] Create `.env` from `.env.example` for real OpenRouter values.
- [x] Update `main.py` to use a direct `user_task` variable (prompt commented out).
- [x] Resolve Playwright MCP Chromium 'chrome' not found issue (install chromium + set `--browser chromium`).
- [x] Switch Playwright MCP integration to standard CrewAI `crewai.mcp` (`MCPServerStdio` via `mcps`).
- [x] Enable CrewAI tracing via `CREWAI_TRACING_ENABLED=true` in `.env` and `.env.example`.
- [x] Add `--timeout-navigation 60000` to Playwright MCP args for slow-loading sites.
- [x] Switch LLM provider from OpenRouter to local LM Studio (commented out OpenRouter).
- [x] Add `docker-compose.yml` for Arize Phoenix tracing/evaluation service.
- [x] Add OpenInference instrumentation packages (crewai, litellm) and arize-phoenix to requirements and install.
- [x] Create `tracing/` module registering Phoenix tracer (project_name = repo name) and import it in `main.py`.
- [x] Make Playwright MCP args dynamic via `config/playwright_config.py` and `build_playwright_args()`.
- [x] Refactor LLM config: common variables in `config/llm_config.py`, single LLM construction in `llm_providers/llm_provider.py`.
- [x] Add `config/phoenix_config.py` for Phoenix settings and use them in registration.

## Next
- [ ] Implement application features per project breakdown.

## Frontend (Streamlit) - Plan
- [x] Add `streamlit` to `requirements.txt` and install.
- [x] Create `frontend/` folder with `app.py`.
- [x] Build basic UI: title, task text input, Run button.
- [x] Connect Run button to `main`/`crew` backend (invoke crew.kickoff with task).
- [ ] Capture and display logs/output in the UI.
- [x] Display final result in the UI.
- [ ] Handle errors and show user-friendly messages.
- [ ] Test end-to-end with a sample task.
