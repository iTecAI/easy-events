from python.easyevents import ASGISourceResponse, EventSourceResponse
from starlite import Starlite, get, Request
import asyncio
import random


@get("/src")
async def test_source(request: Request) -> EventSourceResponse:
    async def gen():
        while True:
            yield {"data": random.random()}
            await asyncio.sleep(1)

    return ASGISourceResponse(gen(), request)


app = Starlite(route_handlers=[test_source])
