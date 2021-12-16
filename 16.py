import functools
import operator


def parse(data, i, versions=None):
    if versions is None:
        versions = []

    versions.append(int(data[i : i + 3], 2))
    type = int(data[i + 3 : i + 6], 2)
    i += 6

    if type == 4:
        num = ""
        done = False
        while not done:
            if data[i] == "0":
                done = True
            num += data[i + 1 : i + 5]
            i += 5
        return (int(num, 2), i, versions)

    values = []
    if data[i] == "0":
        subpackets_length = int(data[i + 1 : i + 16], 2)
        i += 16
        subpackets_start = i

        while i < subpackets_start + subpackets_length:
            value, i, versions = parse(data, i, versions)
            values.append(value)
    else:
        num_packets = int(data[i + 1 : i + 12], 2)
        i += 12
        for _ in range(num_packets):
            value, i, versions = parse(data, i, versions)
            values.append(value)

    if type == 0:
        return (sum(values), i, versions)
    elif type == 1:
        return (functools.reduce(operator.mul, values, 1), i, versions)
    elif type == 2:
        return (min(values), i, versions)
    elif type == 3:
        return (max(values), i, versions)
    elif type == 5:
        return (1 if values[0] > values[1] else 0, i, versions)
    elif type == 6:
        return (1 if values[0] < values[1] else 0, i, versions)
    elif type == 7:
        return (1 if values[0] == values[1] else 0, i, versions)
    else:
        raise ValueError()


with open("16.in") as f:
    input = f.read().strip()

binary = ""
for x in input:
    binary += format(int(x, 16), "b").zfill(4)

res, _, versions = parse(binary, 0)
assert sum(versions) == 925
assert res == 342997120375
print(sum(versions))
print(res)
