from fastapi import APIRouter, HTTPException
from bson.objectid import ObjectId
from mongo_config import collection
from database.schemas import all_tasks
from database.models import TaskBase

router = APIRouter()

@router.get("/all")
def get_all_tasks():
    data = collection.find({"is_deleted": False})
    return all_tasks(data)

@router.get("/{task_id}")
def get_task(task_id: str):
    try:
        existing_task = collection.find_one({"_id": ObjectId(task_id), "is_deleted": False})
        if not existing_task:
            raise HTTPException(status_code=404, detail="Task not found!")
            
        existing_task["_id"] = str(existing_task["_id"])

        task = TaskBase(**existing_task) 
        return {"status_code": 200, "task": task.model_dump()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not retrieve task: {e}")