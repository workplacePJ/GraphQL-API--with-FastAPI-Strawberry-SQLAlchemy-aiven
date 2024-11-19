import strawberry
from typing import Optional
from .queries.invoice import InvoiceQueries
from .mutations.invoice import InvoiceMutations
from .queries.company import CompanyQueries
from .mutations.company import CompanyMutations
from .mutations.auth import AuthMutations

@strawberry.type
class Query(InvoiceQueries, CompanyQueries):
    pass

@strawberry.type
class Mutation(InvoiceMutations, CompanyMutations, AuthMutations):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
