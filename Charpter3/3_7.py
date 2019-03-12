class StrKeyDict0(dict):
    def __missing__(self, key):  # 当处理找不到的key的时候
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]


from collections import UserDict


class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(
            key
        )] = item  # 这个self.data在__getitem__方法中UserDict中该方法的实现就是从self.data中获取结果


if __name__ == '__main__':
    # obj = StrKeyDict0([('2', 'two'), ('4', 'four'), (3, 'three')])
    obj = StrKeyDict([('2', 'two'), ('4', 'four'), (3, 'three')])
    print(obj[3])
    print(obj[2])
    print(obj['4'])
    print(obj.get(3))
    print(obj.get(2))  # get函数不调用getitem 所以这里也不会去调用missing这个函数
