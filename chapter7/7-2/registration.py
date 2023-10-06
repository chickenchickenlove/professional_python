
registry = []

def deco(func):
    print(f'register {func = }')
    registry.append(func)
    return func


@deco
def f1():
    print('f1()')


def f2():
    print('f2()')


@deco
def f3():
    print('f3()')








