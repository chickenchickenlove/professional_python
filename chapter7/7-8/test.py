from functools import singledispatch

sums = 0

@singledispatch
def add(arg):
    global sums
    sums += arg


@add.register
def _(arg: int):
    global sums
    sums += arg


@add.register
def _(arg: float):
    global sums
    sums += arg

@add.register
def _(arg: str):
    global sums
    pass

if __name__ == "__main__":
    add(3)
    add("abc")