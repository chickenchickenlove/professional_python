import functools

registry = []


def decorator_factory(active=True):
    print(active)
    def decorator(func):
        def inner(*args, **kwargs):
            if active:
                registry.append(func)
        return inner
    return decorator

# @decorator_factory(active=True)
def f1():
    print('h')


@decorator_factory
def f3():
    print('hhh')

def f2():
    print('hh')

dec = decorator_factory()
f = dec(f2)


def f4():
    print('hhhggghh')

# print(dec.__code__.co_freevars)
# print(f.__code__.co_freevars)
# print(f.__name__)
#
# print(f1.__name__)

f4 = f3(f4)

f4()

print('he')