import asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from .parsers.price import parse as parse_price_category
from .parsers.sale_q import parse as parse_sale_q
from .parsers.price_history import parse as parse_history
from .db.models import Item, Price


class Runner:
    """
        Класс Runner как пример некоторой сущности которая агрегирует цепочку запросов для получения
        информации об конкретном товаре. В таком сценари используется один httpx клиент, одна сессия, а куки и user-agent
        остаются общими, на одну цепочку запросов, но у каждого экземпляра runner можно сделать собственный клиент httpx.
        Тогда такая цепочка запросов выглядит относительно "естественной".

        :param vendor_code: артикул товара, отправная точка, с помощью артикула можно вытащить почти любую информацию
    """

    def __init__(self, vendor_code: int):
        self.client: AsyncClient = AsyncClient()
        self.vendor_code = vendor_code

    async def to_db(self, data: tuple, async_session: async_sessionmaker[AsyncSession]) -> None:
        async with async_session() as session:
            async with session.begin():
                price = Price(value=data[0].price)
                item = Item(vendor_code=self.vendor_code, category=data[0].category, sale_quantity=data[1].sale_q)
                item.prices.append(price)
                for i in data[2].price_history:
                    item.prices.append(Price(value=i))
                session.add_all([price, item])

    async def run(self, async_session: async_sessionmaker[AsyncSession]) -> None:
        tasks = (
            parse_price_category(self.client, self.vendor_code),
            parse_sale_q(self.client, self.vendor_code),
            parse_history(self.client, self.vendor_code)
        )
        data = await asyncio.gather(*tasks, return_exceptions=True)
        await self.client.aclose()
        await self.to_db(data, async_session)

