import itertools


def enhance(pixels, alg, min_row, max_row, min_col, max_col):
    new_pixels = set()
    for r, c in itertools.product(
        range(min_row, max_row + 1), range(min_col, max_col + 1)
    ):
        pixel = ""
        for dr, dc in itertools.product((-1, 0, 1), (-1, 0, 1)):
            if (r + dr, c + dc) in pixels:
                pixel += "1"
            else:
                pixel += "0"

        if alg[int(pixel, 2)]:
            new_pixels.add((r, c))

    return new_pixels


def solve(pixels, alg, iterations):
    rows = set(x[0] for x in pixels)
    cols = set(x[1] for x in pixels)
    min_row = min(rows) - iterations * 2
    max_row = max(rows) + iterations * 2
    min_col = min(cols) - iterations * 2
    max_col = max(cols) + iterations * 2

    for i in range(iterations):
        pixels = enhance(
            pixels, alg, min_row + i, max_row - i, min_col + i, max_col - i
        )

    return len(pixels)


def main():
    with open("./20.in") as f:
        alg, img = f.read().split("\n\n")

    alg = [x == "#" for x in alg]
    pixels = set()
    for r, row in enumerate(img.splitlines()):
        for c, x in enumerate(row):
            if x == "#":
                pixels.add((r, c))

    p1 = solve(pixels, alg, 2)
    print(p1)
    assert p1 == 5316

    p2 = solve(pixels, alg, 50)
    print(p2)
    assert p2 == 16728


if __name__ == "__main__":
    main()
