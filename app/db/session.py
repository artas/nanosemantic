import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = os.getenv('DB_URL','postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/postgres')

async_engine = create_async_engine(DB_URL, echo=True)
async_session = sessionmaker(async_engine, expire_on_commit=False,
                             class_=AsyncSession)

Base = declarative_base()
