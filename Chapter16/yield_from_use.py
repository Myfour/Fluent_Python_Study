# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        total += new_num
        count += 1
        average = total / count
    # return意味着当前协程结束
    return total, count, average


# 委派生成器
def proxy_gen():
    print('进入委派')
    while True:
        print('开始yield 子生成器')
        total, count, average = yield from average_gen()
        print('结束yield 子生成器')
        print('从子生成器返回了', total, count, average)


# 调用方
if __name__ == '__main__':
    calc_average = proxy_gen()
    next(calc_average)
    print(calc_average.send(10))
    print(calc_average.send(20))
    print(calc_average.send(30))
    calc_average.send(None)
    # 开启新的一个协程
    print(calc_average.send(100))
    print(calc_average.send(22))
    calc_average.send(None)