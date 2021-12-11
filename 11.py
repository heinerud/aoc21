import itertools


def neighbors(grid, r, c):
    nr = [0, -1, -1, -1, 0, 1, 1, 1]
    nc = [1, 1, 0, -1, -1, -1, 0, 1]
    for i, j in ((r + i, c + j) for i, j in zip(nr, nc)):
        if i < 0 or j < 0:
            continue
        if i >= len(grid[0]) or j >= len(grid):
            continue

        yield i, j


def step(grid, r, c):
    grid[r][c] += 1
    if grid[r][c] > 9:
        grid[r][c] = float("-inf")
        for nr, nc in neighbors(grid, r, c):
            step(grid, nr, nc)


def reset(x):
    return 0 if x < 0 else x


with open("11.in") as f:
    grid = [[int(x) for x in l.strip()] for l in f.readlines()]

flashes = 0
for gen in itertools.count(1):
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            step(grid, r, c)

    grid = [[reset(x) for x in row] for row in grid]
    flashes += sum(sum(x == 0 for x in row) for row in grid)

    if gen == 100:
        print(flashes)

    if not sum(sum(row) for row in grid):
        print(gen)
        break
