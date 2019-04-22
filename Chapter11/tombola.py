import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        '''从可迭代对象中添加元素'''

    @abc.abstractmethod
    def pick(self):
        '''随记删除元素，然后返回该元素'''

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))