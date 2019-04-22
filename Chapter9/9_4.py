'''
比较@classmethod和@staticmethod的行为
'''


class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


print(Demo.klassmeth())
print(Demo.klassmeth('aaa'))
print(Demo.statmeth())
print(Demo.statmeth('bbb'))
print(Demo().statmeth())