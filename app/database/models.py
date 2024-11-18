from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database import Base

class Company(Base):
    __tablename__ = "company"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    name_kana = Column(String, nullable=False)
    postal_code = Column(String(7), nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String(11), nullable=False)
    president = Column(String, nullable=False)
    invoice = relationship("Invoice", back_populates="company")

class Invoice(Base):
    __tablename__ = "invoice"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    invoice_number = Column(Integer, autoincrement=True, nullable=False)
    due_date = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False)
    client_name = Column(String, nullable=False)
    total = Column(Float, nullable=False)
    pdf_url = Column(String, nullable=False)
    description = relationship("InvoiceItem", back_populates="invoice")
    company_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=False)
    company = relationship("Company", back_populates="invoice")

class InvoiceItem(Base):
    __tablename__ = "invoice_item"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    item_name = Column(String, nullable=False)
    unit_price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    tax_rate = Column(Integer, nullable=False, default=10)
    amount = Column(Float, nullable=False)
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoice.id"), nullable=False)
    invoice = relationship("Invoice", back_populates="description")

class BankAccount(Base):
    __tablename__ = "bank_account"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bank_name = Column(String, nullable=False)
    branch_name = Column(String, nullable=False)
    account_type = Column(Enum("普通口座", "当座"), nullable=False)
    account_number = Column(String, nullable=False)
    account_holder = Column(String, nullable=False)
    holder_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=False)
