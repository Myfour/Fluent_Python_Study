'''
处理UnicodeEncodeError  处理字符串编码成字节序列错误
'''
city = 'São Paulo'
print(city.encode('utf-8'))
print('---' * 20)

print(city.encode('utf-16'))
print('---' * 20)

try:
    print(city.encode('gb2312'))
except:
    print('出错了')
print('---' * 20)
print(city.encode('gb2312', errors='ignore'))
print('---' * 20)
print(city.encode('gb2312', errors='replace'))
print('---' * 20)
print(city.encode('gb2312', errors='xmlcharrefreplace'))
