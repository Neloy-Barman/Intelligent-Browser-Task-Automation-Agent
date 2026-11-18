# Project Breakdown

## Overview
Intelligent Browser Task Automation Agent — a browser task automation agent powered by CrewAI.

## Current state
- Dependency environment prepared: virtual environment `venv` with CrewAI (tools, litellm) and crewai-tools (mcp) installed.
- `requirements.txt` lists the project dependencies.
- `agents/browser_automation_agent.py` defines a CrewAI `Agent` named `browser_automation_agent` using an OpenRouter LLM.
- `config/llm_config.py` builds the OpenRouter-backed CrewAI `LLM` from environment variables.

## Functionalities
- Browser Automation Agent (CrewAI Agent with role, goal, backstory, llm).
- Browser Automation Task (CrewAI Task with description, expected_output, assigned to browser_automation_agent).
- LLM Config (Variables in config/llm_config.py; common llm provider in llm_providers/llm_provider.py using shared settings).
- Crew (CrewAI Crew orchestrating browser_automation_agent and browser_automation_task).
- Main (Entry point reading user task input and kicking off the crew with interpolation).
- MCP (Playwright MCP server configuration exposed to the agent; args built dynamically from playwright_config.py).
- Docker/Phoenix (docker-compose.yml running Arize Phoenix for tracing and evaluations).
- Instrumentation (OpenInference packages for CrewAI and LiteLLM for tracing/evals).
- Tracing (Phoenix tracer registration under project name = repo name; settings in config/phoenix_settings.py).
