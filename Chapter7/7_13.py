'''
闭包引用环境中的变量是不可变对象时
'''


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager
