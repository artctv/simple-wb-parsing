import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from .models import *


engine = create_async_engine('sqlite+aiosqlite:///sqlite.db')


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
