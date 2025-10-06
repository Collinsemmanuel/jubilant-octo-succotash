from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class TodoStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1, max_length=255)
    status: TodoStatus = Field(default=TodoStatus.PENDING)

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1, max_length=255)
    status: Optional[TodoStatus] = Field(None)

class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = { "from_attributes": True }