from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry

app = FastAPI()

@strawberry.type
class Query:
    hello: str = "Hello, world!"

graphql_app = GraphQLRouter(schema=strawberry.Schema(Query))
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    return {"message": "FastAPI with GraphQL is running!"}
