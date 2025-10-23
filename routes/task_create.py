from fastapi import APIRouter, HTTPException
from mongo_config import collection
from database.models import TaskBase
from database.schemas import CreateTask

router = APIRouter()

@router.post("/create")
def create_task(new_task_data: CreateTask):
    try:
        new_task = TaskBase(**new_task_data.model_dump())
        res = collection.insert_one(new_task.model_dump())
        return {"status_code": 201, "id":str(res.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not create task: {e}")
