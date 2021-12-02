def part_1(input):
    distance = depth = 0
    for direction, n in input:
        n = int(n)
        if direction == "forward":
            distance += n
        elif direction == "down":
            depth += n
        elif direction == "up":
            depth -= n

    return distance * depth


def part_2(input):
    distance = depth = aim = 0
    for direction, n in input:
        n = int(n)
        if direction == "forward":
            distance += n
            depth += aim * n
        elif direction == "down":
            aim += n
        elif direction == "up":
            aim -= n

    return distance * depth


if __name__ == "__main__":
    with open("02.in") as f:
        input = [x.split() for x in f.readlines()]

    print(part_1(input))
    print(part_2(input))
