import asyncio

async def say_hello_slow():
    print("Hello!")
    await asyncio.sleep(2)
    print("Everyone!")


el = asyncio.get_event_loop()
el.run_until_complete(say_hello_slow())
el.close()
