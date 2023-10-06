
def d1(func):
    print('d1')
    return func

def d2(func):
    print('d2')
    return func

@d1
@d2
def f():
    print('f()')







