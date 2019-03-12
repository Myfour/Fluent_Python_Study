import struct
fmt = '<3s3sHH'
with open('haha.gif', 'rb') as fp:
    img = memoryview(fp.read())

headers = img[:10]
print(img)
print(headers)
print(bytes(headers))
print(struct.unpack(fmt, headers))
del headers
del img
