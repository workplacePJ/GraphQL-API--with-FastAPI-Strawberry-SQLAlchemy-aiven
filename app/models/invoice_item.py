from sqlalchemy import Column, String, ForeignKey, Numeric, Integer, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from .mixins import UUIDMixin
from app.core.database import Base

class InvoiceItem(Base, UUIDMixin):
    __tablename__ = "invoice_items"

    item_name = Column(String, nullable=False)
    unit_price = Column(Numeric(precision=12, scale=2), nullable=False)
    quantity = Column(Integer, nullable=False)
    tax_rate = Column(Integer, nullable=False, default=10)
    amount = Column(Numeric(precision=12, scale=2), nullable=False)
    invoice_id = Column(UUID(as_uuid=True), ForeignKey('invoices.id'), nullable=False)

    # リレーションシップ
    invoice = relationship("Invoice", back_populates="items")

    # 制約
    __table_args__ = (
        CheckConstraint('tax_rate >= 1 AND tax_rate <= 99', name='check_tax_rate'),
    )

    @hybrid_property
    def calculate_amount(self):
        return (self.unit_price * self.quantity) + \
               (self.unit_price * self.quantity * self.tax_rate / 100)
