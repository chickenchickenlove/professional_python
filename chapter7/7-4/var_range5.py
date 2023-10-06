
b = 9

def outer():
    def f1(a):
        print(a)
        print(b)

    f1(1)

outer()
