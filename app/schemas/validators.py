import re
from pydantic import field_validator, AnyUrl
from typing import Optional
from datetime import date
from decimal import Decimal

class URLValidator:
    @field_validator('url')
    def validate_url(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            # URLの基本的な検証
            result = AnyUrl(v)
            return str(result)
        except Exception:
            raise ValueError("Invalid URL format")

class JPYPriceValidator:
    @field_validator('price')
    def validate_price(cls, v: Decimal) -> Decimal:
        if v < 0:
            raise ValueError("Price cannot be negative")
        return v.quantize(Decimal('0.01'))

class KanaValidator:
    @field_validator('kana')
    def validate_kana(cls, v: str) -> str:
        if not re.match(r'^[\u30A0-\u30FF\u3000]+$', v):
            raise ValueError("Must contain only full-width katakana characters")
        return v

class PostalCodeValidator:
    @field_validator('postal_code')
    def validate_postal_code(cls, v: str) -> str:
        if not re.match(r'^\d{7}$', v):
            raise ValueError("Must be 7 digits")
        return v
class PhoneValidator:
    @field_validator('phone')
    def validate_phone(cls, v: str) -> str:
        if not re.match(r'^\d{10,11}$', v):
            raise ValueError("Must be 10 or 11 digits")
        return v
