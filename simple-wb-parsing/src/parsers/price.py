from dataclasses import dataclass, asdict
from httpx import AsyncClient
from ..config import URLS
from ..tools import make_request
from .category import parse as parse_category


@dataclass
class CategoryStruct:
    kind_id: int
    subject_id: int
    brand_id: int
    vendor_code: int


@dataclass
class ResultStruct:
    price: int
    category: str


async def parse(client: AsyncClient, vendor_code: int) -> ResultStruct:
    url = URLS.PRICE.format(vendor_code=vendor_code)
    r = await make_request(client, url, "get")
    product = r["data"]["products"][0]
    price = product.get("salePriceU")
    if not price:
        price = price.get("priceU")

    # конвертация из формата рубликопейки в рубли.копейки
    # price = price[:len(str(price))-2] + "." + price[len(str(price))-2:]

    kind_id = product["kindId"]
    subject_id = product["subjectId"]
    brand_id = product["brandId"]

    category = await parse_category(client, asdict(CategoryStruct(kind_id, subject_id, brand_id, vendor_code)))
    return ResultStruct(price, category)


