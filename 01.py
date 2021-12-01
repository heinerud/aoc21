def increasing(l, d=1):
    for a, b in zip(l[:-d], l[d:]):
        yield b > a


if __name__ == "__main__":
    with open("01.in") as f:
        entries = [int(x) for x in f.readlines()]

    print(sum(increasing(entries, 1)))
    print(sum(increasing(entries, 3)))
