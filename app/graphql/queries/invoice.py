from typing import List, Optional
import strawberry
from uuid import UUID
from app.graphql.types.invoice import Invoice, InvoiceFilter, InvoiceSort
from app.core.security import decode_token
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.models.invoice import Invoice as InvoiceModel

@strawberry.type
class InvoiceQueries:
    @strawberry.field
    async def invoice(self, info, id: UUID) -> Optional[Invoice]:
        async with info.context["session"] as session:
            query = select(InvoiceModel).options(
                selectinload(InvoiceModel.items)
            ).where(InvoiceModel.id == id)
            result = await session.execute(query)
            invoice = result.scalar_one_or_none()
            return invoice

    @strawberry.field
    async def invoices(
        self,
        info,
        filter: Optional[InvoiceFilter] = None,
        sort: Optional[InvoiceSort] = None,
        skip: int = 0,
        limit: int = 10
    ) -> List[Invoice]:
        async with info.context["session"] as session:
            query = select(InvoiceModel).options(
                selectinload(InvoiceModel.items)
            )

            # フィルター適用
            if filter:
                if filter.client_name:
                    query = query.where(InvoiceModel.client_name.ilike(f"%{filter.client_name}%"))
                if filter.created_at_start:
                    query = query.where(InvoiceModel.created_at >= filter.created_at_start)
                if filter.created_at_end:
                    query = query.where(InvoiceModel.created_at <= filter.created_at_end)
                if filter.due_date_start:
                    query = query.where(InvoiceModel.due_date >= filter.due_date_start)
                if filter.due_date_end:
                    query = query.where(InvoiceModel.due_date <= filter.due_date_end)

            # ソート適用
            if sort:
                if sort.created_at:
                    query = query.order_by(
                        InvoiceModel.created_at.asc()
                        if sort.created_at == "ASC"
                        else InvoiceModel.created_at.desc()
                    )
                if sort.due_date:
                    query = query.order_by(
                        InvoiceModel.due_date.asc()
                        if sort.due_date == "ASC"
                        else InvoiceModel.due_date.desc()
                    )

            query = query.offset(skip).limit(limit)
            result = await session.execute(query)
            return result.scalars().all()
