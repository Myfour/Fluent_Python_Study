registry = []


def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func


@register
def f1():
    print('f1() is running~~')


print('running main()')
print(f'registry -> {registry}')
f1()