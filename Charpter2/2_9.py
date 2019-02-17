# 命名元组
from collections import namedtuple

City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.coordinates)
print(tokyo[1])

print(City._fields)

LatLong = namedtuple('LatLong', ['lat', 'long'])
delhi = City('Delhi NCR', 'IN', 21.935, LatLong(28.323, 90.231))
print(delhi)
print(delhi._asdict())
