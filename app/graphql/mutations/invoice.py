from typing import Optional
import strawberry
from uuid import UUID
from app.graphql.types.invoice import Invoice, CreateInvoiceInput, UpdateInvoiceInput
from app.services.invoice import InvoiceService
from app.core.security import decode_token

@strawberry.type
class InvoiceMutations:
    @strawberry.mutation
    async def create_invoice(self, info, input: CreateInvoiceInput) -> Invoice:
        token = info.context["request"].headers.get("Authorization")
        if not token or not decode_token(token.split(" ")[1]):
            raise Exception("Unauthorized")

        async with info.context["session"] as session:
            invoice_service = InvoiceService(session)
            return await invoice_service.create_invoice(input)

    @strawberry.mutation
    async def update_invoice(self, info, input: UpdateInvoiceInput) -> Invoice:
        token = info.context["request"].headers.get("Authorization")
        if not token or not decode_token(token.split(" ")[1]):
            raise Exception("Unauthorized")

        async with info.context["session"] as session:
            invoice_service = InvoiceService(session)
            return await invoice_service.update_invoice(input)

    @strawberry.mutation
    async def delete_invoice(self, info, id: UUID) -> bool:
        token = info.context["request"].headers.get("Authorization")
        if not token or not decode_token(token.split(" ")[1]):
            raise Exception("Unauthorized")

        async with info.context["session"] as session:
            invoice_service = InvoiceService(session)
            return await invoice_service.delete_invoice(id)
