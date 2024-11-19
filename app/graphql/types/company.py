from typing import List, Optional
import strawberry
from uuid import UUID
from .base import TimestampMixin
from app.models.enums import AccountType

@strawberry.type
class BankAccount:
    id: UUID
    bank_name: str
    branch_name: str
    account_type: AccountType
    account_number: str
    account_holder: str
    holder_id: UUID

@strawberry.input
class BankAccountInput:
    bank_name: str
    branch_name: str
    account_type: AccountType
    account_number: str
    account_holder: str

@strawberry.type
class Company(TimestampMixin):
    id: UUID
    name: str
    name_kana: str
    postal_code: str
    address: str
    building_name: Optional[str]
    room_number: Optional[str]
    phone: str
    fax: Optional[str]
    mail: Optional[str]
    hp: Optional[str]
    president: str
    company_seal: Optional[str]
    business_name: Optional[str]
    business_name_kana: Optional[str]
    business_hp: Optional[str]
    business_sns_links: Optional[str]
    bank_accounts: List[BankAccount]

@strawberry.input
class CreateCompanyInput:
    name: str
    name_kana: str
    postal_code: str
    address: str
    building_name: Optional[str] = None
    room_number: Optional[str] = None
    phone: str
    fax: Optional[str] = None
    mail: Optional[str] = None
    hp: Optional[str] = None
    president: str
    company_seal: Optional[str] = None
    business_name: Optional[str] = None
    business_name_kana: Optional[str] = None
    business_hp: Optional[str] = None
    business_sns_links: Optional[str] = None
    bank_accounts: Optional[List[BankAccountInput]] = None

@strawberry.input
class UpdateCompanyInput:
    id: UUID
    name: Optional[str] = None
    name_kana: Optional[str] = None
    postal_code: Optional[str] = None
    address: Optional[str] = None
    building_name: Optional[str] = None
    room_number: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    mail: Optional[str] = None
    hp: Optional[str] = None
    president: Optional[str] = None
    company_seal: Optional[str] = None
    business_name: Optional[str] = None
    business_name_kana: Optional[str] = None
    business_hp: Optional[str] = None
    business_sns_links: Optional[str] = None
    bank_accounts: Optional[List[BankAccountInput]] = None
