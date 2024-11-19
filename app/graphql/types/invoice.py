from typing import List, Optional
import strawberry
from datetime import date
from decimal import Decimal
from uuid import UUID
from .base import TimestampMixin, SortDirection

@strawberry.type
class InvoiceItem:
    id: UUID
    item_name: str
    unit_price: Decimal
    quantity: int
    tax_rate: int
    amount: Decimal
    invoice_id: UUID

@strawberry.input
class InvoiceItemInput:
    item_name: str
    unit_price: Decimal
    quantity: int
    tax_rate: Optional[int] = 10

@strawberry.type
class Invoice(TimestampMixin):
    id: UUID
    invoice_number: str
    due_date: Optional[date]
    client_name: str
    total: Decimal
    pdf_url: str
    company_id: UUID
    items: List[InvoiceItem]

@strawberry.input
class InvoiceFilter:
    client_name: Optional[str] = None
    created_at_start: Optional[date] = None
    created_at_end: Optional[date] = None
    due_date_start: Optional[date] = None
    due_date_end: Optional[date] = None

@strawberry.input
class InvoiceSort:
    created_at: Optional[SortDirection] = None
    due_date: Optional[SortDirection] = None

@strawberry.input
class CreateInvoiceInput:
    due_date: Optional[date] = None
    client_name: str
    company_id: UUID
    items: List[InvoiceItemInput]

@strawberry.input
class UpdateInvoiceInput:
    id: UUID
    due_date: Optional[date] = None
    client_name: Optional[str] = None
    items: Optional[List[InvoiceItemInput]] = None
