from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from uuid import UUID

class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class TimestampSchema(BaseSchema):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class IDSchema(BaseSchema):
    id: UUID
