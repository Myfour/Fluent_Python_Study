def deco(func):
    def inner():
        print('running inner()')

    return inner


def target():
    print('running target()')


target()


@deco
def target1():
    print('running target1()')


target()