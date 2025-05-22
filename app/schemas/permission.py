# app/schemas/permission.py

from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    owner = "owner"
    editor = "editor"
    viewer = "viewer"

class ShareUser(BaseModel):
    user_id: int
    role: RoleEnum

class ShareRequest(BaseModel):
    users: list[ShareUser]
