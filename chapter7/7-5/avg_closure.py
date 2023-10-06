
def make_average():
    series = []

    def average(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return average

Avg = make_average()

print(Avg(1))

print(f'{Avg.__code__.co_freevars = }')
print(f'{Avg.__closure__ = }')
print(f'{Avg.__closure__[0].cell_contents = }')
