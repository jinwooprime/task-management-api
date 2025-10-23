from pydantic import BaseModel, ConfigDict
from typing import Optional

class CreateTask(BaseModel):
    model_config = ConfigDict(extra="forbid") # prevents any additional attributes/fields from being inputted in request body.

    title: str
    description: str
    is_completed: Optional[bool] = False

class UpdateTask(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

def individual_task(task):
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "status": "Completed" if task["is_completed"] else "In progress"
    }

def all_tasks(tasks):
    return [individual_task(task) for task in tasks]