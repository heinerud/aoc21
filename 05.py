import collections
import itertools


def ranger(a, b):
    if a > b:
        return range(a, b - 1, -1)
    return range(a, b + 1)


with open("05.in") as f:
    input = (x.strip() for x in f.readlines())

c1 = collections.Counter()
c2 = collections.Counter()
for l in input:
    x1, y1, x2, y2 = (int(x) for x in l.replace("->", ",").split(","))
    if x1 == x2 or y1 == y2:  # Horizontal or vertical
        points = list(itertools.product(ranger(x1, x2), ranger(y1, y2)))
        c1.update(points)
        c2.update(points)

    else:  # Assume diagonal
        points = zip(ranger(x1, x2), ranger(y1, y2))
        c2.update(points)

print(sum(x > 1 for x in c1.values()))
print(sum(x > 1 for x in c2.values()))
