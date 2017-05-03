# aiocoincheck: Async Coincheck Api Library

aiocoincheck は [coincheck](https://coincheck.com) をasync/awaitに対応させたものです。

```
import asyncio
from coincheck import market

async def main():
    m1 = market.Market()
    result = await m1.ticker()  # await を使う場合はpython3.5以上必須
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

ドキュメントの詳細は本家を参照ください。

## Environment

- support Python 3.4~

## Installation


### git

```
git clone git@github.com:soy-curd/aiocoincheck.git
```

### pip 

```
pip install git+https://github.com/soy-curd/aiocoincheck
```
