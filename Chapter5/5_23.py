'''
itemgetter 简单使用
'''
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter

for city in sorted(
        metro_data, key=itemgetter(2)):  # itemgetter()实例返回的是一个函数对象，该函数可以调用
    print(city)

print('--' * 20)
print(itemgetter(2)(metro_data))

print('--' * 20)

cc = itemgetter(1, 0)
for city in metro_data:
    print(cc(city))