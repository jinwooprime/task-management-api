from fastapi import APIRouter, HTTPException, Depends, Request
from bson.objectid import ObjectId
from mongo_config import collection
from datetime import datetime

router = APIRouter()

'''
This function ensures that no request body is sent.
'''
async def reject_body(request: Request):
    body = await request.body()
    if body:
        raise HTTPException(status_code=400, detail="Request body is not allowed!")

@router.patch("/recover/{task_id}")
async def recover_task(task_id:str, _: None = Depends(reject_body)):
    try:
        id = ObjectId(task_id)
        existing_task = collection.find_one({"_id": id})
        if not existing_task:
            raise HTTPException(status_code=404, detail=f"Task does not exist!")
        if not existing_task.get("is_deleted", True):
            raise HTTPException(status_code=400, detail="Task already exists!")

        collection.update_one(
            {"_id": id}, 
            {"$set": {
                "is_deleted": False,
                "updated_at": int(datetime.timestamp(datetime.now()))
            }}
        )

        return {"status_code": 200, "message": "Task successfully recovered!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not recover task: {e}")