import heapq
import itertools
from collections import defaultdict, Counter, deque

with open("15.in") as f:
    grid = [[int(x) for x in l] for l in f.read().splitlines()]


def neighbors(grid, r, c):
    for dr, dc in ((0, 1), (-1, 0), (0, -1), (1, 0)):
        nr, nc = r + dr, c + dc
        if nr < 0 or nc < 0 or nr >= len(grid[0]) or nc >= len(grid):
            continue

        yield nr, nc


def solve(grid):
    rows, cols = len(grid), len(grid[0])
    distance = [[None for _ in row] for row in grid]
    q = [(0, 0, 0)]
    while q:
        (d, r, c) = heapq.heappop(q)
        d += grid[r][c]
        if distance[r][c] is None or d < distance[r][c]:
            distance[r][c] = d
        else:
            continue

        if r == rows - 1 and c == cols - 1:
            break

        for nr, nc in neighbors(grid, r, c):
            heapq.heappush(q, (distance[r][c], nr, nc))

    # plot(distance, grid, r, c)

    return distance[rows - 1][cols - 1] - grid[0][0]


def path(distance, r, c):
    while True:
        yield r, c
        min = distance[r][c]
        for nr, nc in neighbors(distance, r, c):
            if distance[nr][nc] < min:
                r, c = nr, nc

        if min == distance[r][c]:
            break


def plot(distance, grid, r, c):
    grid = [[x for x in r] for r in grid]
    for r, c in path(distance, r, c):
        grid[r][c] = "."

    for r in grid:
        print("".join(str(x) for x in r))


def increment(grid, n):
    new_grid = []
    for i, r in enumerate(grid):
        new_row = []
        for j, x in enumerate(r):
            x += n
            while x > 9:
                x -= 9
            new_row.append(x)
        new_grid.append(new_row)
    return new_grid


def extend(grid, n):
    grid_down = []
    for n in range(n):
        grid_down += increment(grid, n)

    grid_right = increment(grid_down, 0)
    for n in range(1, n + 1):
        grid_right = [a + b for a, b in zip(grid_right, increment(grid_down, n))]
    return grid_right


print(solve(grid))
print(solve(extend(grid, 5)))
