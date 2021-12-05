from collections import defaultdict


def ranger(a, b):
    if a > b:
        return reversed(range(b, a + 1))
    if b > a:
        return range(a, b + 1)

    raise ValueError("same")


with open("05.in") as f:
    input = [x.strip().replace("->", ",").split(",") for x in f.readlines()]
input = [[int(x) for x in e] for e in input]
coordinates = [[(x[0], x[1]), (x[2], x[3])] for x in input]

points = defaultdict(int)
for p1, p2 in coordinates:
    if p1[0] == p2[0]:
        for n in ranger(p1[1], p2[1]):
            p = (p1[0], n)
            points[p] += 1

    elif p1[1] == p2[1]:
        for n in ranger(p1[0], p2[0]):
            p = (n, p1[1])
            points[p] += 1

print(len([x for x in points.values() if x > 1]))

points = defaultdict(int)
for p1, p2 in coordinates:
    if p1[0] == p2[0]:
        for n in ranger(p1[1], p2[1]):
            p = (p1[0], n)
            points[p] += 1

    elif p1[1] == p2[1]:
        for n in ranger(p1[0], p2[0]):
            p = (n, p1[1])
            points[p] += 1

    else:
        for a, b in zip(ranger(p1[0], p2[0]), ranger(p1[1], p2[1])):
            p = (a, b)
            points[p] += 1


print(len([x for x in points.values() if x > 1]))
