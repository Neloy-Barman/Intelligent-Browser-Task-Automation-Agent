from crewai import Task

from agents.browser_automation_agent import browser_automation_agent


browser_automation_task = Task(
    description="""
The user wants you to do this web task:

{user_task}

First write a short numbered plan. Then carry it out in the browser, verifying
each step. If a step fails, replan and try a different tool or approach until
the task is complete or you are clearly blocked.
""",

    expected_output="""
The final result of the task only, stated plainly and directly.
Do not include the steps taken, explanations, or extra commentary.
""",

    agent=browser_automation_agent,
    verbose=True,
)
