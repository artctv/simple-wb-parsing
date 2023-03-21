from httpx import AsyncClient
from ..config import URLS
from ..tools import make_request


async def parse(client: AsyncClient, url_param: dict) -> str:
    url = URLS.CATEGORY.format(**url_param)
    r = await make_request(client, url, "get")
    site_path = r["value"]["data"]["sitePath"]
    category_path = ""
    for i in site_path:
        category_path += "{}/".format(i["name"])

    return category_path
