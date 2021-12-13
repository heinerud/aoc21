with open("13.in") as f:
    positions, folds = f.read().split("\n\n")


dots = set()
for xy in positions.splitlines():
    x, y = xy.split(",")
    dots.add((int(x), int(y)))

for gen, fold in enumerate(folds.splitlines()):
    axis, i = fold.replace("fold along ", "").split("=")
    i = int(i)

    d = set()
    if axis == "y":
        for x, y in dots:
            if y < i:
                d.add((x, y))
            elif y > i:
                d.add((x, i - (y - i)))
    elif axis == "x":
        for x, y in dots:
            if x < i:
                d.add((x, y))
            elif x > i:
                d.add((i - (x - i), y))

    dots = d

    if gen == 0:
        print(len(dots))

rows = max(x[1] for x in dots) + 1
cols = max(x[0] for x in dots) + 1
grid = [[" "] * cols for _ in range(rows)]
for x, y in dots:
    grid[y][x] = "@"

for r in grid:
    print("".join(r))
