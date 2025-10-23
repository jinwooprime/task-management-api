from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    _id: Optional[str] = None
    title: str
    description: str
    is_completed: bool = False
    is_deleted: bool = False
    updated_at: int = Field(default_factory=lambda: int(datetime.timestamp(datetime.now())))
    created_at: int = Field(default_factory=lambda: int(datetime.timestamp(datetime.now())))