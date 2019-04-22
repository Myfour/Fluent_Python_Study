'''
计算移动平均值
使用协程
'''


def averger():
    total = 0.0
    count = 0
    averger = None
    while True:
        tmp = yield averger
        total += tmp
        count += 1
        averger = total / count


if __name__ == '__main__':
    avg = averger()
    print(next(avg))
    print(avg.send(10))
    print(avg.send(50))
    print(avg.send(50))
    print(avg.send(50))
    print(avg.send(50))
