import asyncio


# python 3.5支持了新的协程语法
async def hello(name):
    await asyncio.sleep(3)
    print('hello', name)


def hello_2(name):
    # yield from asyncio.sleep(1)
    yield
    print('hello2', name)


corountine = hello('world')
corountine_2 = hello_2('GOD')
loop = asyncio.get_event_loop()
# task = loop.create_task(corountine)
to_do = asyncio.wait([corountine, corountine_2])
loop.run_until_complete(to_do)
