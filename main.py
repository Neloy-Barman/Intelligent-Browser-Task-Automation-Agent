import os
import shutil
import sys

# Register Phoenix tracing for this project (global registration).
import tracing.phoenix_tracing  # noqa: F401

from config.playwright_config import PLAYWRIGHT_SNAPSHOT_DIR
from crew import crew


def main():
    # Direct task input (edit this value as needed)
    # user_task = "Visit https://qa-playground-automation-testing.onrender.com/ and provide the names of all available products."

    user_task = "Visit https://qa-playground-automation-testing.onrender.com/ and tell me what this website is about."

    # Prompt-based input (commented out for now)
    # user_task = input("Enter the browser automation task: ").strip()
    # if not user_task:
    #     print("No task provided. Exiting.")
    #     sys.exit(1)

    try:
        result = crew.kickoff(inputs={"user_task": user_task})
        print("\nResult:\n", result)
    finally:
        # Clean up Playwright MCP generated snapshot files
        shutil.rmtree(PLAYWRIGHT_SNAPSHOT_DIR, ignore_errors=True)


if __name__ == "__main__":
    main()
