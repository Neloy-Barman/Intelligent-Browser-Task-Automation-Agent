from crewai import Task

from agents.browser_automation_agent import browser_automation_agent


browser_automation_task = Task(
    description="""
Automate the following browser task: {task}.
Navigate the target website and perform the required interactions.
""",
    expected_output="""
A concise summary of the actions performed
and the information extracted from the browser.
""",
    agent=browser_automation_agent,
)
