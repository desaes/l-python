import asyncio

async def say_hello():
    print("Hello!")

el = asyncio.get_event_loop()
el.run_until_complete(say_hello())
el.close()
