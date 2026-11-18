from crewai import Task

from agents.browser_automation_agent import browser_automation_agent


browser_automation_task = Task(
    description="""
The user wants you to do this web task:

{user_task}

Break down the given task into smaller steps. Map proper tools to each step.
Build a checklist. Perform the plan steps. Reach the final response.
""",

    expected_output="""
The result requested by the user, stated clearly and in a well-formatted way.
""",

    agent=browser_automation_agent,
    verbose=True,
)
