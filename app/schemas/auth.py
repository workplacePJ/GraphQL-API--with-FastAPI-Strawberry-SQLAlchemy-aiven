from pydantic import EmailStr
from .base import BaseSchema

class Token(BaseSchema):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenPayload(BaseSchema):
    sub: str | None = None
    refresh: bool = False

class UserAuth(BaseSchema):
    email: EmailStr
    password: str

class UserCreate(UserAuth):
    full_name: str

class User(BaseSchema):
    email: EmailStr
    full_name: str
    is_active: bool = True
