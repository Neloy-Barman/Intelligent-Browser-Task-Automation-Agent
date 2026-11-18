from crewai import Agent
from crewai_tools import FileReadTool

from config.agents_config import (
    BROWSER_AGENT_BACKSTORY,
    BROWSER_AGENT_GOAL,
    BROWSER_AGENT_ROLE,
)
from llm_providers import llm
from mcp_servers.playwright_mcp import playwright_mcp_server

# MCP servers available to this agent (standard crewai.mcp approach).
agent_mcps = [playwright_mcp_server,]

browser_automation_agent = Agent(
    role=BROWSER_AGENT_ROLE,
    goal=BROWSER_AGENT_GOAL,
    backstory=BROWSER_AGENT_BACKSTORY,
    llm=llm,
    mcps=agent_mcps,
    tools=[FileReadTool()],
    verbose=True,
)
