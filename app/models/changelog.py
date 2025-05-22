from sqlalchemy import Column, Integer, DateTime, ForeignKey, JSON
from datetime import datetime
from app.db.base import Base


class EventChangelog(Base):
    __tablename__ = "event_changelog"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    version_from = Column(Integer)
    version_to = Column(Integer)
    diff = Column(JSON)
    changed_by = Column(Integer, ForeignKey("users.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
