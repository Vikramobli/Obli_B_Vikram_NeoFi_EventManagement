from sqlalchemy import Column, Integer, DateTime, ForeignKey, JSON
from datetime import datetime, timezone
from app.db.base import Base

class EventVersion(Base):
    __tablename__ = "event_versions"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    modified_by = Column(Integer, ForeignKey("users.id"))
    data_snapshot = Column(JSON)
    timestamp = Column(DateTime, default=lambda: datetime.now(tz=timezone.utc))
