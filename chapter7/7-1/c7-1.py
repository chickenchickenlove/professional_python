
def deco(func):
    print(f'function Name = {func}')

    def inner():
        print('running inner()')
    return inner


@deco
def target1():
    print('running target()')


@deco
def target2():
    print('running target()')


print('===== start1 =====')
target1()

print('===== start2 =====')
hello = deco(target1)
hello()

print('===== start3 =====')
deco(target1)()





