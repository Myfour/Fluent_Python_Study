from math import hypot

# 一些魔术方法的使用
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__=='__main__':
    v=Vector(2,1)
    print(v)
    print(abs(v))
    print(v+Vector(2,4))
    print(v*5)