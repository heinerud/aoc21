def increasing(l):
    for a, b in zip(l[:-1], l[1:]):
        yield b > a


def windows(l):
    for a, b, c in zip(l[:-2], l[1:-1], l[2:]):
        yield sum((a, b, c))


if __name__ == "__main__":
    with open("01.in") as f:
        entries = [int(x) for x in f.readlines()]

    print(sum(increasing(entries)))
    print(sum(increasing(list(windows(entries)))))
