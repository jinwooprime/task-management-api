from fastapi import APIRouter, HTTPException
from bson.objectid import ObjectId
from mongo_config import collection

router = APIRouter()

# This route permanently deletes a task.
@router.delete("/perm_delete/{task_id}")
def delete_permanent(task_id: str):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id": id})
        if not existing_doc:
            raise HTTPException(status_code=404, detail=f"Task not found!")

        collection.delete_one({"_id": id})

        return {"status_code": 200, "message": "Task has been permanently deleted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not permanently delete task: {e}")
