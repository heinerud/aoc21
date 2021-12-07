import statistics

with open("07.in") as f:
    input = f.readline()

crabs = [int(x) for x in input.split(",")]

median = int(statistics.median(crabs))
fuel = (abs(x - median) for x in crabs)
print(sum(fuel))

mean = int(statistics.mean(crabs))
fuel = (sum(range(1, abs(x - mean) + 1)) for x in crabs)
print(sum(fuel))
