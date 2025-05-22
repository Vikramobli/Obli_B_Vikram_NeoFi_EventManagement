# Directory: app/schemas/event.py
from pydantic import BaseModel
from typing import Optional

class EventCreate(BaseModel):
    title: str
    description: Optional[str]
    start_time: str
    end_time: str
    location: Optional[str]
    is_recurring: bool
    recurrence_pattern: Optional[str]

class EventUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    start_time: Optional[str]
    end_time: Optional[str]
    location: Optional[str]
    is_recurring: Optional[bool]
    recurrence_pattern: Optional[str]

class EventOut(BaseModel):
    id: int
    title: str
    start_time: str
    end_time: str