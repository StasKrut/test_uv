# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "aiohttp>2",
#     "asyncio",
#     "rich",
# ]
# ///
import asyncio

import aiohttp
from rich.pretty import pprint


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        ) as response:
            data = await response.json()
            pprint([(k, v["rate_float"]) for k, v in data["bpi"].items()][:10])


asyncio.run(main())
