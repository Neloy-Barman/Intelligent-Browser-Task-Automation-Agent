# Playwright MCP integration for CrewAI (standard crewai.mcp approach).
#
# CrewAI provides native MCP support via `MCPServerStdio`, which lets an Agent
# connect to an MCP server over stdio. The args are built dynamically from
# `config/playwright_config.py` so flags are only added when their values
# are present.

from crewai.mcp import MCPServerStdio

from config.playwright_config import (
    PLAYWRIGHT_BROWSER,
    PLAYWRIGHT_CODEGEN,
    PLAYWRIGHT_HEADLESS,
    PLAYWRIGHT_TIMEOUT_ACTION,
    PLAYWRIGHT_TIMEOUT_NAVIGATION,
    PLAYWRIGHT_TIMEOUT_SETTLE,
)


def build_playwright_args() -> list[str]:
    args = ["-y", "@playwright/mcp@latest"]

    if PLAYWRIGHT_HEADLESS:
        args.append("--headless")
    if PLAYWRIGHT_BROWSER:
        args.append(f"--browser={PLAYWRIGHT_BROWSER}")
    if PLAYWRIGHT_TIMEOUT_NAVIGATION is not None:
        args.append(f"--timeout-navigation={PLAYWRIGHT_TIMEOUT_NAVIGATION}")
    if PLAYWRIGHT_TIMEOUT_ACTION is not None:
        args.append(f"--timeout-action={PLAYWRIGHT_TIMEOUT_ACTION}")
    if PLAYWRIGHT_TIMEOUT_SETTLE is not None:
        args.append(f"--timeout-settle={PLAYWRIGHT_TIMEOUT_SETTLE}")
    if PLAYWRIGHT_CODEGEN:
        args.append(f"--codegen={PLAYWRIGHT_CODEGEN}")

    return args


playwright_mcp_server = MCPServerStdio(
    command="npx",
    args=build_playwright_args(),
)

# Alternative: expose only browser_navigate via CrewAI's tool_filter
# from crewai.mcp.filters import create_static_tool_filter
#
# playwright_mcp_server_navigate_only = MCPServerStdio(
#     command="npx",
#     args=build_playwright_args(),
#     tool_filter=create_static_tool_filter(
#         allowed_tool_names=["browser_navigate"]
#     ),
# )
