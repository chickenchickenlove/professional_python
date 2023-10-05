

def make_average():
    series = []
    series2 = []

    def averager(new_value):
        series.append(new_value)
        series2.append(new_value)
        ret = sum(series) / len(series)
        print(ret)
        return ret

    return averager

avg1 = make_average()
avg1(10)
avg1(11)
avg1(12)
avg1(13)
avg1(14)
avg1(15)

print(avg1.__code__.co_freevars)
for clo in avg1.__closure__:
    print(clo)
# print(avg1.__closure__)





