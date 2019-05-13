import asyncio

# 使用async创建一个协程
async def execute(x):
    print('Number:', x)
    return x


coroutine = execute(1) # 实例化这个函数，生成一个协程，但是函数内部并未执行
print('Corontime-->:', coroutine)
print('After calling execute(1)-->')

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print('After calling loop')