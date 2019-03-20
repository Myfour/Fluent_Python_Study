'''提取函数签名'''
from clip import clip, clip_a
from inspect import signature

sig = signature(clip)
print(repr(sig))
print(str(sig))

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

'''函数注解'''
print(clip.__annotations__)  # 未提供注解，所以__annotations中是空的
print(clip_a.__annotations__)