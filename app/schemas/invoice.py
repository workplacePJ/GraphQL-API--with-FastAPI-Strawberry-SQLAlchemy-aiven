from pydantic import HttpUrl, Field
from typing import List, Optional
from datetime import date
from decimal import Decimal
from uuid import UUID
from .base import BaseSchema, IDSchema, TimestampSchema
from .invoice_item import InvoiceItem

class InvoiceBase(BaseSchema):
    due_date: Optional[date] = None
    client_name: str
    total: Decimal = Field(gt=0)

class InvoiceCreate(InvoiceBase):
    company_id: UUID
    items: List[InvoiceItem]

class InvoiceUpdate(InvoiceBase):
    due_date: Optional[date] = None
    client_name: str | None = None
    total: Decimal | None = None
    items: List[InvoiceItem] | None = None

class InvoiceInDB(InvoiceBase, IDSchema, TimestampSchema):
    invoice_number: str
    pdf_url: HttpUrl
    company_id: UUID
    items: List[InvoiceItem] = []

class InvoiceFilter(BaseSchema):
    client_name: Optional[str] = None
    created_at_start: Optional[date] = None
    created_at_end: Optional[date] = None
    due_date_start: Optional[date] = None
    due_date_end: Optional[date] = None

class InvoiceSort(BaseSchema):
    created_at: Optional[bool] = None  # True for ascending, False for descending
    due_date: Optional[bool] = None    # True for ascending, False for descending

Invoice = InvoiceInDB
