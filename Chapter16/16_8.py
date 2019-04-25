'''
协程中的异常处理
'''


class DemoException(Exception):
    '''
    为演示的异常类型
    '''


def demo_exc_handling():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException Handled. Continuing...')
            else:
                print('-> coroutine recieved:{!r}'.format(x))
        raise RuntimeError('This is never run.')
    finally:
        print('-> coroutine ending')


if __name__ == '__main__':
    exc_coro = demo_exc_handling() # 创建这个协程的实例
    next(exc_coro)  # 预激这个协程
    exc_coro.send(10)
    # exc_coro.close()
    exc_coro.throw(DemoException) # gen.throw()用于抛出一个异常
    exc_coro.send(20)
    # exc_coro.throw(ZeroDivisionError)
    exc_coro.close()  # gen.close()用于关闭一个协程