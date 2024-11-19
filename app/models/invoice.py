from sqlalchemy import Column, String, Date, Integer, ForeignKey, Numeric, func, select
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from .mixins import TimestampMixin, UUIDMixin
from app.core.database import Base

class Invoice(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "invoices"

    invoice_number = Column(String, unique=True, nullable=False)
    due_date = Column(Date, nullable=True)
    client_name = Column(String, nullable=False)
    total = Column(Numeric(precision=12, scale=2), nullable=False)
    pdf_url = Column(String, nullable=False)
    company_id = Column(UUID(as_uuid=True), ForeignKey('companies.id'), nullable=False)

    # リレーションシップ
    company = relationship("Company", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")

    @classmethod
    async def generate_invoice_number(cls, session):
        # 最後のインボイス番号を取得
        query = select(func.substring(cls.invoice_number, 3)
                      .cast(Integer)
                      .label('last_num')) \
                .order_by(func.substring(cls.invoice_number, 3).cast(Integer).desc()) \
                .limit(1)
        result = await session.execute(query)
        last_num = result.scalar()
        
        # 新しい番号を生成
        next_num = 1 if last_num is None else last_num + 1
        return f"oS{str(next_num).zfill(8)}"
