import queue


def neighbors(grid, row, col):
    rc = ((row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col))
    for r, c in rc:
        if r < 0 or c < 0:
            continue
        try:
            yield grid[r][c], r, c
        except IndexError:
            continue


def basin(grid, row, col):
    points = set()
    points.add((grid[row][col], row, col))

    q = queue.Queue()
    q.put((row, col))

    while not q.empty():
        for n in neighbors(grid, *q.get()):
            if n in points:
                continue

            x, r, c = n
            if x < 9:
                points.add(n)
                q.put((r, c))

    return points


with open("09.in") as f:
    grid = [[int(x) for x in r.strip()] for r in f.readlines()]


low_points = []
for i, row in enumerate(grid):
    for j, x in enumerate(row):
        if all(x < n for n, _, _ in neighbors(grid, i, j)):
            low_points.append((i, j))

print(sum(grid[r][c] + 1 for r, c in low_points))

basins = (basin(grid, r, c) for r, c in low_points)
product = 1
for b in sorted(len(b) for b in basins)[-3:]:
    product *= b

print(product)
