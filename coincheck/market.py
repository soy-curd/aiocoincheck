import ast
import aiohttp

"""
document: https://coincheck.com/documents/exchange/api
"""

base_url = "https://coincheck.com"
api_urls = {"ticker": "/api/ticker",
            "trades": "/api/trades",
            "order_books": "/api/order_books"
            }


class Market(object):
    def __init__(self):
        pass

    async def public_api(self, url):
        """ template function of public api"""
        async with aiohttp.ClientSession() as session:
            async with session.get(base_url + api_urls.get(url)) as res:
                text = await res.text()
                return ast.literal_eval(text)

    async def ticker(self):
        """get latest information of coincheck market"""
        return await self.public_api("ticker")

    async def trades(self):
        """get latest deal history of coincheck market"""
        return await self.public_api("trades")

    async def orderbooks(self):
        """get latest asks/bids information of coincheck market"""
        return await self.public_api("order_books")


if __name__ == "__main__":
    pass
