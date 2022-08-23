import datetime
import math
import asyncio

def main():
    el = asyncio.get_event_loop()
    start = datetime.datetime.now()
    #el.run_until_complete(compute(start=1, end=50_000_000))
    task1 = el.create_task(compute(start=1, end=10_000_000))
    task2 = el.create_task(compute(start=10_000_001, end=20_000_000))
    task3 = el.create_task(compute(start=20_000_001, end=30_000_000))
    task4 = el.create_task(compute(start=30_000_001, end=40_000_000))
    task5 = el.create_task(compute(start=40_000_001, end=50_000_000))
    tasks = asyncio.gather(task1, task2, task3, task4, task5)
    el.run_until_complete(tasks)
    elapsed = datetime.datetime.now() - start

    print(f'Elpased time: {elapsed.total_seconds():.2f} seconds.')

async def compute(start, end=1):
    pos = start
    factor = 1000 * 1000
    while pos < end:
        pos += 1
        math.sqrt((pos - factor) * (pos - factor))

if __name__ == '__main__':
    main()

"""
Elpased time: 8.11 seconds.
"""