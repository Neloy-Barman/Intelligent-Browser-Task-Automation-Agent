import shutil

from config.playwright_config import PLAYWRIGHT_SNAPSHOT_DIR


def cleanup_playwright_snapshots(result):
    """Callback run after crew kickoff to remove Playwright MCP snapshot files."""
    shutil.rmtree(PLAYWRIGHT_SNAPSHOT_DIR, ignore_errors=True)
    return result
