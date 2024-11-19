from pydantic import Field
from decimal import Decimal
from .base import BaseSchema, IDSchema
from uuid import UUID

class InvoiceItemBase(BaseSchema):
    item_name: str
    unit_price: Decimal = Field(gt=0)
    quantity: int = Field(gt=0)
    tax_rate: int = Field(ge=1, le=99, default=10)

class InvoiceItemCreate(InvoiceItemBase):
    pass

class InvoiceItemUpdate(InvoiceItemBase):
    item_name: str | None = None
    unit_price: Decimal | None = None
    quantity: int | None = None
    tax_rate: int | None = None

class InvoiceItemInDB(InvoiceItemBase, IDSchema):
    invoice_id: UUID
    amount: Decimal

InvoiceItem = InvoiceItemInDB
