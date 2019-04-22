class Foo:
    def __getitem__(self, pos):
        return range(50)[pos]

print('--------支持索引---------')
f = Foo()
print(f[10])
print('--------支持迭代--底层机制实现根据索引从0递增去迭代---------')  
for x in f:
    print(x)
print('--------支持成员 in操作---------')
print(20 in f, 60 in f)
