
def make_average():
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total

        count += 1
        total += new_value
        return total / count

    return average

Avg = make_average()

print(Avg(1))

print(f'{Avg.__code__.co_freevars = }')
print(f'{Avg.__closure__ = }')
print(f'{Avg.__closure__[0].cell_contents = }')
