def reverse(word):
    return word[::-1]


fruits = ['straberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits, key=reverse))

# sorted就是一个高阶函数 