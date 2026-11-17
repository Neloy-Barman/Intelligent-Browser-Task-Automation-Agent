from crewai import Agent

from config.llm_config import llm
from mcp_config.playwright_mcp import playwright_mcp_server


# MCP servers available to this agent (standard crewai.mcp approach).
agent_mcps = [playwright_mcp_server,]

browser_automation_agent = Agent(
    role="Browser Automation Agent",
    goal="""
Automate browser tasks by navigating pages,
interacting with elements, and extracting information.
""",
    backstory="""
You are an intelligent agent specialized in automating
web browser interactions to accomplish user tasks efficiently and reliably.
""",
    llm=llm,
    mcps=agent_mcps,
    verbose=True,
)
