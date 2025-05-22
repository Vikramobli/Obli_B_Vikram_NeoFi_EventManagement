from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.event import EventCreate, EventUpdate, EventOut
from app.services.event_service import create_event, list_events, get_event, update_event, delete_event, create_batch_events

router = APIRouter()

@router.post("/", response_model=EventOut)
def create(data: EventCreate):
    return create_event(data)

@router.get("/")
def list():
    return list_events()

@router.get("/{id}")
def get(id: int):
    return get_event(id)

@router.put("/{id}")
def update(id: int, data: EventUpdate):
    return update_event(id, data)

@router.delete("/{id}")
def delete(id: int):
    return delete_event(id)

@router.post("/batch")
def batch_create(data: List[EventCreate]): # type: ignore
    return create_batch_events(data)