from coincheck.utils import make_header
import simplejson as json
import aiohttp

"""
document: https://coincheck.com/documents/exchange/api
"""


class Account(object):
    def __init__(self,
                 access_key=None,
                 secret_key=None):
        self.access_key = access_key
        self.secret_key = secret_key

    async def get_info(self):
        """ show user information
        """

        url = "https://coincheck.com/api/accounts"
        headers = make_header(url,
                              access_key=self.access_key,
                              secret_key=self.secret_key)

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as res:
                text = await res.text()
                return json.loads(text)

    async def get_balance(self):
        """ confirm balance
        """
        url = "https://coincheck.com/api/accounts/balance"
        headers = make_header(url,
                              access_key=self.access_key,
                              secret_key=self.secret_key)
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as res:
                text = await res.text()
                return json.loads(text)


if __name__ == "__main__":
    pass
