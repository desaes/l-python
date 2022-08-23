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

def main():
    total = 5000
    data = asyncio.Queue()

    el = asyncio.get_event_loop()
    task1 = el.create_task(gen_data(total, data))
    task2 = el.create_task(gen_data(total, data))
    task3 = el.create_task(process_data(total * 2, data))

    tasks = asyncio.gather(task1, task2, task3)
    el.run_until_complete(tasks)
    


if __name__ == '__main__':
    main()