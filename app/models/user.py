from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from datetime import datetime , timezone

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(tz=timezone.utc))
