import asyncio
from src.runner import Runner
from src.db.provider import engine, create_tables
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


# вставьте сюда свой артикул товара
VENDOR_CODE: int = 0


async def main(vendor_code):
    await create_tables()
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    runner = Runner(vendor_code)
    await runner.run(async_session)
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main(VENDOR_CODE))
