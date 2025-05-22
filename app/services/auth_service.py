# Directory: app/services/auth_service.py
# NOTE: This is a placeholder for JWT auth logic
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, Token
from app.models.user import User
from app.db.session import SessionLocal
from app.utils.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/api/auth")

def register_user(data):
    db = SessionLocal()
    db_user = User(username=data.username, email=data.email, hashed_password=hash_password(data.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = create_access_token({"sub": str(db_user.id)})
    return {"access_token": "mock", "token_type": "bearer"}

def login_user(data):
    db = SessionLocal()
    db_user = db.query(User).filter(User.email == data.email).first()
    if not db_user or not verify_password(data.password, db_user.hashed_password):
        raise HTTPException(401, detail="Invalid credentials")
    token = create_access_token({"sub": str(db_user.id)})
    return {"access_token": "mock", "token_type": "bearer"}

def refresh_token():
    return {"access_token": "mock", "token_type": "bearer"}

def logout_user():
    return {"message": "Logged out"}