import array
number = array.array('h', [-3, -2, -1, 0, 1, 2])
print(number)
memv = memoryview(number)
print(memv)
print(memv[0])
print(memv.tolist())
memv_oct = memv.cast('B')
print(memv_oct.tolist())