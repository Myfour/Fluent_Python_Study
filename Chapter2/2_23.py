# deque 双向队列
from collections import deque
dq = deque(range(10), 10)  # 第二个参数为这个队列的大小
print(dq)
dq.rotate(3)  # 双向队列的翻转操作，把右边的3个元素翻转到左边
print(dq)
dq.rotate(-4)  # 反过来右边4个到左边
print(dq)
dq.appendleft(-1)  # 队列的左边添加一个元素，由于双向队列的大小为10，当左侧添加新元素后挤走了右侧第一个元素
print(dq)  # 反之 右侧添加元素会挤走左侧的元素
dq.extend([11, 12, 13])
print(dq)
dq.extendleft([-5, -4])
print(dq)