from pydantic import EmailStr, HttpUrl, Field
from typing import Optional, List
from .base import BaseSchema, IDSchema, TimestampSchema
from .bank_account import BankAccount
from .validators import KanaValidator, PostalCodeValidator, PhoneValidator

class CompanyBase(BaseSchema, KanaValidator, PostalCodeValidator, PhoneValidator):
    name: str
    name_kana: str
    postal_code: str
    address: str
    building_name: Optional[str] = None
    room_number: Optional[str] = None
    phone: str
    fax: Optional[str] = None
    mail: Optional[EmailStr] = None
    hp: Optional[HttpUrl] = None
    president: str
    company_seal: Optional[HttpUrl] = None
    business_name: Optional[str] = None
    business_name_kana: Optional[str] = None
    business_hp: Optional[HttpUrl] = None
    business_sns_links: Optional[HttpUrl] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    name: str | None = None
    name_kana: str | None = None
    postal_code: str | None = None
    address: str | None = None
    phone: str | None = None
    president: str | None = None

class CompanyInDB(CompanyBase, IDSchema, TimestampSchema):
    bank_accounts: List[BankAccount] = []

Company = CompanyInDB
