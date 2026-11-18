from crewai import Crew, Process

from agents.browser_automation_agent import browser_automation_agent
from callbacks.crew_callbacks import cleanup_playwright_snapshots
from tasks.browser_automation_task import browser_automation_task


crew = Crew(
    agents=[browser_automation_agent],
    tasks=[browser_automation_task],
    process=Process.sequential,
    verbose=True,
    after_kickoff_callbacks=[cleanup_playwright_snapshots],
)
