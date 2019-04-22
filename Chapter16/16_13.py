'''
让协程返回值
'''
from collections import namedtuple
Result = namedtuple('Result', 'count average')


def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


if __name__ == '__main__':
    avg = average()
    next(avg)
    print(avg.send(10))
    print(avg.send(10))
    print(avg.send(10))
    # print(avg.send(None))
    try:
        print(avg.send(None))
    except StopIteration as e:
        print(e.value)