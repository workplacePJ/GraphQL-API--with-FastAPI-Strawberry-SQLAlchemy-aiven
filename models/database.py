from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from decouple import config

DATABASE_URL = config('POSTGRES_DB_URL')
#DATABASE_URL = 'postgresql+asyncpg://<username>:<password>@<host>/<database>'
#DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format('postgresql+asyncpg', 'admin', 'password', 'db', '5432', 'async_db')

engine = create_async_engine(DATABASE_URL, echo=True)
DBSession = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def get_db():
    async with DBSession() as session:
        yield session
