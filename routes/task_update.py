from fastapi import APIRouter, HTTPException
from bson.objectid import ObjectId
from mongo_config import collection
from datetime import datetime
from database.schemas import UpdateTask

router = APIRouter()

@router.put("/update/{task_id}")
def update_task(task_id: str, updated_task_data: UpdateTask):
    try:
        id = ObjectId(task_id)
        existing_task = collection.find_one({"_id": id, "is_deleted": False})
        if not existing_task:
            raise HTTPException(status_code=404, detail=f"Task does not exist!")
        
        update_data = updated_task_data.model_dump(exclude_unset=True) # 'exclude_unset=True' Gets only fields that were sent in the request.
        
        update_data["updated_at"] = int(datetime.timestamp(datetime.now()))
        
        collection.update_one(
            {"_id": id}, 
            {"$set": update_data}
        )
        
        return {"status_code": 200, "message": "Task updated successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not update task: {e}")
