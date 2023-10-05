def f1(a):
    print(a)
    print(b)

b = 6
f1(3)


def f2(a):
    # global b
    print(a)

    # b에 대해서 global을 사용하지 않으면 에러가 발생함.
    # 파이썬은 함수를 컴파일 할 때, 함수 본체 안에서 할당된 변수는 local 변수로 판단하기 때문임.
    # 그래서 이 경우, local 변수 b가 바인딩 되지 않았다는 것을 알게 됨. (local variable 'b' referenced before assignment)
    print(b)
    b = 9

f2(3)
