from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .mixins import TimestampMixin, UUIDMixin
from app.core.database import Base

class Company(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "companies"

    name = Column(String, nullable=False)
    name_kana = Column(String, nullable=False)
    postal_code = Column(String(7), nullable=False)
    address = Column(String, nullable=False)
    building_name = Column(String)
    room_number = Column(String)
    phone = Column(String, nullable=False)
    fax = Column(String)
    mail = Column(String)
    hp = Column(String)
    president = Column(String, nullable=False)
    company_seal = Column(String)
    business_name = Column(String)
    business_name_kana = Column(String)
    business_hp = Column(String)
    business_sns_links = Column(String)

    # リレーションシップ
    bank_accounts = relationship("BankAccount", back_populates="company", cascade="all, delete-orphan")
    invoices = relationship("Invoice", back_populates="company", cascade="all, delete-orphan")
