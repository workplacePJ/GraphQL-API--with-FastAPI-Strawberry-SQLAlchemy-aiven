from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
import pytz

class TimestampMixin:
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone('Asia/Tokyo')))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone('Asia/Tokyo')), onupdate=lambda: datetime.now(pytz.timezone('Asia/Tokyo')))

class UUIDMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
