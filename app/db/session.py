# app/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")


if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in the environment.")


connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# For SQLite, check_same_thread=False is needed for multi-threading support
engine = create_engine(
    DATABASE_URL, connect_args=connect_args, 
    pool_pre_ping=True # helps prevent stale DB connections
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)