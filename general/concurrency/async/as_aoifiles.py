import asyncio
import aiofiles
import sys, os


async def example_file1():
    async with aiofiles.open(os.getcwd() + '/dev/l-python/general/concurrency/async/' + 'texto.txt') as fd:
        data = await fd.read()
    print(data)

async def example_file2():
    async with aiofiles.open(os.getcwd() + '/dev/l-python/general/concurrency/async/' + 'texto.txt') as fd:
        async for line in fd:
            print(line)


def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(example_file2())
    el.close()

if __name__ == '__main__':
    main()
    