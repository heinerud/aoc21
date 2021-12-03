def most_frequent(l):
    return "0" if l.count("0") > l.count("1") else "1"


def part_1(input):
    gamma = ""
    for i in range(len(input[0])):
        l = [x[i] for x in input]
        gamma += most_frequent(l)

    epsilon = gamma.replace("1", "x").replace("0", "1").replace("x", "0")

    return int(epsilon, 2) * int(gamma, 2)


def part_2(input):
    oxygen = [x for x in input]
    co2 = [x for x in input]
    for i in range(len(input[0])):
        if len(oxygen) > 1:
            keep_oxygen = most_frequent([x[i] for x in oxygen])
            oxygen = [x for x in oxygen if x[i] == keep_oxygen]

        if len(co2) > 1:
            keep_co2 = most_frequent([x[i] for x in co2])
            keep_co2 = "0" if keep_co2 == "1" else "1"
            co2 = [x for x in co2 if x[i] == keep_co2]

    return int(oxygen[0], 2) * int(co2[0], 2)


if __name__ == "__main__":
    with open("03.in") as f:
        input = [x.strip() for x in f.readlines()]

    print(part_1(input))
    print(part_2(input))
