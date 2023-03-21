from dataclasses import dataclass
from httpx import AsyncClient
from ..config import URLS
from ..tools import make_request


@dataclass
class ResultStruct:
    sale_q: int


async def parse(client: AsyncClient, vendor_code: int) -> ResultStruct:
    url = URLS.SALE_QUANTITY.format(vendor_code=vendor_code)
    r = await make_request(client, url, "get")
    sale_q = r[0]["qnt"]
    return ResultStruct(sale_q)
