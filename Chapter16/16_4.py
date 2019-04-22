'''
预激协程的装饰器
'''
from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        print('预激完成........')
        return gen

    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    averager = None
    while True:
        term = yield averager
        total += term
        count += 1
        averager = total / count


if __name__ == '__main__':
    co_avg = averager()
    from inspect import getgeneratorstate
    print(getgeneratorstate(co_avg))
    print(co_avg.send(10))
    print(co_avg.send(20))
    print(co_avg.send(20))
    print('---------------------')
    print(averager.__name__)
