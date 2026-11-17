# Playwright MCP integration for CrewAI (standard crewai.mcp approach).
#
# CrewAI provides native MCP support via `MCPServerStdio`, which lets an Agent
# connect to an MCP server over stdio. The args are built dynamically from
# `config/playwright_config.py` so flags are only added when their values
# are present.

from crewai.mcp import MCPServerStdio

from config.playwright_config import (
    PLAYWRIGHT_BROWSER,
    PLAYWRIGHT_HEADLESS,
    PLAYWRIGHT_TIMEOUT_ACTION,
    PLAYWRIGHT_TIMEOUT_NAVIGATION,
    PLAYWRIGHT_TIMEOUT_SETTLE,
)


def build_playwright_args() -> list[str]:
    args = ["-y", "@playwright/mcp@latest"]

    if PLAYWRIGHT_BROWSER:
        args += ["--browser", PLAYWRIGHT_BROWSER,]
    if PLAYWRIGHT_HEADLESS:
        args.append("--headless")
    if PLAYWRIGHT_TIMEOUT_NAVIGATION is not None:
        args += ["--timeout-navigation", str(PLAYWRIGHT_TIMEOUT_NAVIGATION),]
    if PLAYWRIGHT_TIMEOUT_ACTION is not None:
        args += ["--timeout-action", str(PLAYWRIGHT_TIMEOUT_ACTION),]
    if PLAYWRIGHT_TIMEOUT_SETTLE is not None:
        args += ["--timeout-settle", str(PLAYWRIGHT_TIMEOUT_SETTLE),]

    return args


playwright_mcp_server = MCPServerStdio(
    command="npx",
    args=build_playwright_args(),
)
