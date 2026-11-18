# Playwright MCP settings.
# These are not secrets, so they live in a regular module instead of .env.
PLAYWRIGHT_BROWSER = "chrome"  # chrome, chromium, firefox, webkit, msedge
PLAYWRIGHT_HEADLESS = True  # Run the browser in headless mode when True
PLAYWRIGHT_TIMEOUT_NAVIGATION = 60000  # ms; set to None to use the default
PLAYWRIGHT_TIMEOUT_ACTION = None  # ms; set to None to use the default
PLAYWRIGHT_TIMEOUT_SETTLE = None  # ms; set to None to use the default
PLAYWRIGHT_CODEGEN = (
    "python"  # codegen language: typescript, python, java, csharp, none
)
# Folder where Playwright MCP saves generated snapshot files.
PLAYWRIGHT_SNAPSHOT_DIR = ".playwright-mcp"
