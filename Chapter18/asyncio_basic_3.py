import asyncio
import requests


async def request():
    url = 'http://localhost:5000'
    status = requests.get(url)
    return status


def callback(task):
    print('回调的结果,Status:', task.result())


coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)  # Task对象添加回调函数
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
