from typing import Optional
from dataclasses import dataclass
from httpx import AsyncClient
from ..config import URLS
from ..tools import make_request


@dataclass
class ResultStruct:
    price_history: list[int]


async def parse(client: AsyncClient, vendor_code: int) -> Optional[ResultStruct]:
    for i in range(0, 15):
        if i < 10:
            n = "0"+str(i)
        else:
            n = i
        url = URLS.PRICE_HISTORY.format(
            vendor_code=vendor_code,
            vendor_code_first_three=str(vendor_code)[:3],
            vendor_code_first_five=str(vendor_code)[:5],
            server_n=n
        )
        r = await make_request(client, url, "get")
        if r is not None:
            break
    else:
        return None

    history = []
    for i in r:
        history.append(i["price"]["RUB"])
    return ResultStruct(price_history=history)