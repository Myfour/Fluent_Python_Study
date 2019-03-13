'''
字节序列转字符串时的解码错误UnicodeDecodeError
'''
octets = b'Montr\xe9al'
print(octets.decode('cp1252'))

print(octets.decode('koi8_r'))

try:
    print(octets.decode('utf-8'))
except:
    print('解码错误')

print(octets.decode('utf-8', errors='replace'))
