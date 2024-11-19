from pydantic import Field
from .base import BaseSchema, IDSchema
from uuid import UUID
from app.models.enums import AccountType

class BankAccountBase(BaseSchema):
    bank_name: str
    branch_name: str
    account_type: AccountType
    account_number: str
    account_holder: str

class BankAccountCreate(BankAccountBase):
    holder_id: UUID

class BankAccountUpdate(BankAccountBase):
    bank_name: str | None = None
    branch_name: str | None = None
    account_type: AccountType | None = None
    account_number: str | None = None
    account_holder: str | None = None

class BankAccountInDB(BankAccountBase, IDSchema):
    holder_id: UUID

BankAccount = BankAccountInDB
