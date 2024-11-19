import strawberry
from datetime import datetime, date
from decimal import Decimal
from uuid import UUID
from typing import TypeVar, Generic, Optional
from enum import Enum

@strawberry.type
class TimestampMixin:
    created_at: datetime
    updated_at: datetime

@strawberry.type
class Error:
    message: str
    code: str

T = TypeVar("T")

@strawberry.type
class PageInfo:
    has_next_page: bool
    has_previous_page: bool
    start_cursor: Optional[str] = None
    end_cursor: Optional[str] = None

@strawberry.type
class Connection(Generic[T]):
    page_info: PageInfo
    edges: list[T]
    total_count: int

@strawberry.enum
class SortDirection(Enum):
    ASC = "asc"
    DESC = "desc"
