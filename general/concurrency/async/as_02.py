import datetime
import asyncio
from pkgutil import get_data

async def gen_data(amount: int, data: asyncio.Queue):
    print(f'Wait until {amount} units of data are created...')
    for idx in range(1, amount + 1):
        item = idx * idx
        await data.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)
    print(f'{amount} data generated')

async def process_data(amount: int, data: asyncio.Queue):
    print(f'Wait until {amount} units of data are processed...')
    processed = 0
    while processed < amount:
        await data.get()
        processed = processed + 1
        await asyncio.sleep(0.001)
    print(f'Processed {amount} data')

async def main():
    total = 5000
    data = asyncio.Queue()
    
    await gen_data(total, data)
    await gen_data(total, data)
    await process_data(total * 2, data)

if __name__ == '__main__':
    el = asyncio.get_event_loop()
    el.run_until_complete(main())
    el.close()