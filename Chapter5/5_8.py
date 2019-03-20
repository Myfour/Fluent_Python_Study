'''
使用__call__实现一个类的可调用
'''
import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except LookupError:
            raise LookupError('pick from empty BingoCase')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    a = BingoCage(range(3))
    print(a._items)
    print(a())
    print(a())
    print(a())
    print(a())