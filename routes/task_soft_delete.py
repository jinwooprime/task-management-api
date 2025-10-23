from fastapi import APIRouter, HTTPException
from bson.objectid import ObjectId
from mongo_config import collection

router = APIRouter()

# This soft-deletes a task, meaning it can be recovered if the 'is_deleted' flag is set to True.
@router.delete("/soft_delete/{task_id}")
def delete_task(task_id: str):
    try:
        id = ObjectId(task_id)
        existing_task = collection.find_one({"_id": id, "is_deleted": False})
        if not existing_task:
            raise HTTPException(status_code=404, detail=f"Task does not exist!")

        collection.update_one({"_id": id}, {"$set":{"is_deleted": True}})

        return {"status_code": 200, "message": "Task has been soft-deleted successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not soft-delete task: {e}")
