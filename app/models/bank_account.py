from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .mixins import UUIDMixin
from .enums import AccountType
from app.core.database import Base

class BankAccount(Base, UUIDMixin):
    __tablename__ = "bank_accounts"

    bank_name = Column(String, nullable=False)
    branch_name = Column(String, nullable=False)
    account_type = Column(Enum(AccountType), nullable=False)
    account_number = Column(String, nullable=False)
    account_holder = Column(String, nullable=False)
    holder_id = Column(UUID(as_uuid=True), ForeignKey('companies.id'), nullable=False)

    # リレーションシップ
    company = relationship("Company", back_populates="bank_accounts")
