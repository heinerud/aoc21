from collections import deque

with open("06.in") as f:
    input = f.readline()

fish = deque(input.count(x) for x in "876543210")

for i in range(256):
    if i == 80:
        print(sum(fish))

    fish.rotate()
    fish[-7] += fish[0]

print(sum(fish))
