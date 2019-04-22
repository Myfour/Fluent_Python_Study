'''
装饰器何时被执行
'''
registry = []


def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()

'''
>>>
running register(<function f1 at 0x000001ED72562840>)
running register(<function f2 at 0x000001ED72B8E268>)
running main()
registry -> [<function f1 at 0x000001ED72562840>, <function f2 at 0x000001ED72B8E268>]
running f1()
running f2()
running f3()
'''