# app/routes/collaboration.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.permission import EventPermission, RoleEnum
from app.db.base import Base
from app.models.event import Event
from app.schemas.permission import ShareRequest
from app.utils.dependencies import get_current_user



router = APIRouter(prefix="/api/events")


class PermissionUpdateRequest(Base):
    role: RoleEnum

@router.post("/{id}/share")
def share_event(id: int, payload: ShareRequest, db: Session = Depends(SessionLocal), current_user=Depends(get_current_user)):
    event = db.query(Event).filter(Event.id == id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Check current_user is the owner
    permission = db.query(EventPermission).filter_by(event_id=id, user_id=current_user.id).first()

    if not permission or permission.role != RoleEnum.owner:  # type: ignore
        raise HTTPException(status_code=403, detail="Only owners can perform this action")

    # Add or update permissions
    for user in payload.users:
        existing = db.query(EventPermission).filter_by(event_id=id, user_id=user.user_id).first()
        if existing:
            existing.role = user.role # type: ignore
        else:
            db.add(EventPermission(event_id=id, user_id=user.user_id, role=user.role))

    db.commit()
    return {"message": "Permissions updated successfully"}



@router.get("/{id}/permissions")
def get_permissions(id: int, db: Session = Depends(SessionLocal), current_user=Depends(get_current_user)):
    # Check if user has any permission on the event
    permission = db.query(EventPermission).filter_by(event_id=id, user_id=current_user.id).first()
    if not permission:
        raise HTTPException(status_code=403, detail="Access denied")

    permissions = db.query(EventPermission).filter_by(event_id=id).all()
    return [{"user_id": p.user_id, "role": p.role} for p in permissions]



@router.put("/{id}/permissions/{user_id}")
def update_permission(id: int, user_id: int, body: PermissionUpdateRequest, db: Session = Depends(SessionLocal), current_user=Depends(get_current_user)):
    # Ensure current user is the owner
    owner_permission = db.query(EventPermission).filter_by(event_id=id, user_id=current_user.id).first()
    if not owner_permission or owner_permission.role != RoleEnum.owner: #type:ignore
        raise HTTPException(status_code=403, detail="Only owners can update permissions")

    perm = db.query(EventPermission).filter_by(event_id=id, user_id=user_id).first()
    if not perm:
        raise HTTPException(status_code=404, detail="Permission not found")

    perm.role = body.role #type:ignore
    db.commit()
    return {"message": "Permission updated"}



@router.delete("/{id}/permissions/{user_id}")
def delete_permission(id: int, user_id: int, db: Session = Depends(SessionLocal), current_user=Depends(get_current_user)):
    owner_permission = db.query(EventPermission).filter_by(event_id=id, user_id=current_user.id).first()
    if not owner_permission or owner_permission.role != RoleEnum.owner:  #type:ignore
        raise HTTPException(status_code=403, detail="Only owners can remove permissions")

    perm = db.query(EventPermission).filter_by(event_id=id, user_id=user_id).first()
    if not perm:
        raise HTTPException(status_code=404, detail="Permission not found")

    db.delete(perm)
    db.commit()
    return {"message": "Permission removed"}






