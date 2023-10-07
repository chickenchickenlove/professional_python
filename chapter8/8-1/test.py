
class Gizmo:
    def __init__(self):
        print(f'Gizmo id: {id(self)}')

x = Gizmo()

# Traceback (most recent call last):
#   File "C:\dev\proessional_python\chapter8\8-1\test.py", line 7, in <module>
#     y = Gizmo() * 10
# TypeError: unsupported operand type(s) for *: 'Gizmo' and 'int'
# Gizmo id: 1821490323808
# Gizmo id: 1821490325056
# y = Gizmo() * 10을 할 때, Gizmo()가 먼저 호출된다. -> 즉, 객체를 먼저 생성하고 '변수'라는 별명을 붙이려고 함.
y = Gizmo() * 10
