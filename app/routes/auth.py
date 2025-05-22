from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserLogin, Token
from app.services.auth_service import register_user, login_user, refresh_token, logout_user

router = APIRouter()

@router.post("/register", response_model=Token)
def register(data: UserCreate):
    return register_user(data)

@router.post("/login", response_model=Token)
def login(data: UserLogin):
    return login_user(data)

@router.post("/refresh")
def refresh():
    return refresh_token()

@router.post("/logout")
def logout():
    return logout_user()