from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config

SQLALCHEMY_DATABASE_URL = config('POSTGRES_DB_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo = True)
DBSession = sessionmaker(bind = engine, autoflush = False)
Base = declarative_base() 




from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+asyncpg://<username>:<password>@<host>/<database>"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session
