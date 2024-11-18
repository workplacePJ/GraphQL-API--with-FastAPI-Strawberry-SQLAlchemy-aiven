from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database import Base

class BankAccount(Base):
    __tablename__ = 'bank_account'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bank_name = Column(String, nullable=False)
    branch_name = Column(String, nullable=False)
    account_type = Column(Enum('普通口座', '当座'), nullable=False)
    account_number = Column(String, nullable=False)
    account_holder = Column(String, nullable=False)
    holder_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=False)
