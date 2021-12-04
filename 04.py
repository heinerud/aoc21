class Board:
    def __init__(self, grid):
        self.rows = [set(x) for x in grid + list(zip(*grid))]
        self.numbers = set.union(*self.rows)

    def bingo(self, numbers):
        return any(r.issubset(numbers) for r in self.rows)

    def sum_unmarked(self, numbers):
        return sum(self.numbers - numbers)


def int_grid(g):
    return [[int(x) for x in l.split()] for l in g.splitlines()]


def part_1(bingo_numbers, grids):
    boards = [Board(int_grid(g)) for g in grids]
    visited = set()

    for n in bingo_numbers:
        visited.add(n)
        for b in boards:
            if b.bingo(visited):
                return n * b.sum_unmarked(visited)


def part_2(bingo_numbers, grids):
    boards = [Board(int_grid(g)) for g in grids]
    visited = set()

    for n in bingo_numbers:
        visited.add(n)
        for b in boards:
            if b.bingo(visited):
                boards.remove(b)

            if len(boards) == 0:
                return n * b.sum_unmarked(visited)


if __name__ == "__main__":
    with open("04.in") as f:
        bingo_numbers, *grids = f.read().split("\n\n")

    bingo_numbers = [int(x) for x in bingo_numbers.split(",")]
    print(part_1(bingo_numbers, grids))
    print(part_2(bingo_numbers, grids))
