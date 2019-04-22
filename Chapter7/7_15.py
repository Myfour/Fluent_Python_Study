'''
实现一个装饰器

用来计算函数用时
'''

import time
from functools import wraps  # 可以不用


def clock(func):
    # @wraps(func)
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print(f'[{end:.8}] {name}({arg_str}) -> {result}')
        return result

    return clocked


if __name__ == '__main__':

    @clock
    def snooze(seconds, name='test'):
        time.sleep(seconds)
        print(name)

    snooze(.123,name='haha')
    print(snooze.__name__)
    # @clock
    # def factorial(n):
    #     return 1 if n < 2 else n * factorial(n - 1)

    # factorial(6)
