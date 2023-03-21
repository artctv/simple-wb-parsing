import asyncio
from httpx import AsyncClient, HTTPError


async def make_request(client: AsyncClient, url: str, method: str, timeout=5) -> dict:
    """Дженерик асинхронный запрос в общем виде"""
    try:
        r = await client.request(url=url, method=method, timeout=timeout)
        r.raise_for_status()
    except HTTPError as exc:
        pass
        # print(f"HTTP Exception for {exc.request.url} - {exc}")
        # some log here
    except asyncio.CancelledError as e:
        pass
        # print(f"Canceled by other task: {e}")
        # some log here
    else:
        return r.json()
