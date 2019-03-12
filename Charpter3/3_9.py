'''
不可变的映射类型
'''
from types import MappingProxyType

d = {'1': 'one', '2': 'two'}
proxy_d = MappingProxyType(d)
print(d, proxy_d)
print(proxy_d['1'], proxy_d['2'])
# proxy_d['3'] = 'three'  # 不可变映射不可以修改，是只读的，但是其与他映射的对象是相互连接的
d['3'] = 'three'
print(d, proxy_d)
print(proxy_d['3'])
