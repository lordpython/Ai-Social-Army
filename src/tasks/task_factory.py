from crewai import Task
from typing import Any, Optional

def create_task(description: str, expected_output: str, agent: Any, context: Optional[list] = None):
    task = Task(description=description, expected_output=expected_output, agent=agent)
    if context:
        task.context = context
    return task