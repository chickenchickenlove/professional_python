import functools

"""
데코레이터 팩토리를 이용해 매개변수화 된 데코레이터를 생성하는 과정은 다음과 같이 이해하자.

@decorator_factory()
def f1():
    ...

-> decorator_factory()는 decorator를 반환하니까.
@decorator
def f1():
    ...

그리고 데코레이터 팩토리의 매개변수들은 각 함수 객체의 클로저를 통해서 전달된다.
func.__code__.co_freevars를 통해서 확인할 수 있음. 

"""


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