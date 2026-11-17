# Playwright MCP integration for CrewAI (standard crewai.mcp approach).
#
# CrewAI provides native MCP support via `MCPServerStdio`, which lets an Agent
# connect to an MCP server over stdio. We define the Playwright MCP server here
# and pass it to the Agent through its `mcps` argument.

from crewai.mcp import MCPServerStdio

# MCPServerStdio describes how to spawn the Playwright MCP server process.
# `command` is the executable and `args` are its arguments. Using `-y` makes
# npx install/run @playwright/mcp without an interactive prompt. `--browser
# chromium` selects the Chromium browser (installed via
# `npx playwright install chromium`).
playwright_mcp_server = MCPServerStdio(
    command="npx",
    args=[
        "-y",
        "@playwright/mcp@latest",
        "--browser",
        "chrome",
        # "firefox",
    ],
)
