'''
元组的相对不可变性
'''

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
# 两者的标识
print(id(t1), id(t2))
print(t1 is t2)

# 字符串的不可变
t3 = 'str'
t4 = 'str'
print(t3 == t4)
print(t3 is t4)

# 元组的相对不可变是对于元组汇总的元素的标识
print(id(t1[2]))
t1[2].append(50)
print(t1)
print(id(t1[2]))  # 元组的不可变是指元素的标识不可变

# 不可变的元素时不可变的
# t1[0] = 'str'
