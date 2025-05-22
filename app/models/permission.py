# app/models/event_permission.py

from sqlalchemy import Column, Integer, ForeignKey, Enum
from app.db.base import Base
import enum

class RoleEnum(str, enum.Enum):
    owner = "owner"
    editor = "editor"
    viewer = "viewer"

class EventPermission(Base):
    __tablename__ = "event_permissions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    role = Column(Enum(RoleEnum))
