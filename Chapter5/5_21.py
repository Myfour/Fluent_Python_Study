from functools import reduce


def fact(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


if __name__ == '__main__':
    print(fact(3))
