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
- LLM Config (OpenRouter provider, model and API key from environment).
- Crew (CrewAI Crew orchestrating browser_automation_agent and browser_automation_task).
- Main (Entry point reading user task input and kicking off the crew with interpolation).
- MCP (Playwright MCP server configuration exposed to the agent).
