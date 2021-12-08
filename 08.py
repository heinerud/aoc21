import collections
import statistics

with open("08.in") as f:
    input = [x.split(" | ") for x in f.readlines()]

input = [(signals.split(), output.split()) for signals, output in input]

c = collections.Counter()
for _, output in input:
    c.update(len(x) for x in output)

# 1, 4, 7 and 8
print(c[2] + c[4] + c[3] + c[7])

result = 0
for signals, output in input:
    keys = [None] * 10
    lengths = [len(x) for x in signals]
    keys[1] = signals[lengths.index(2)]
    keys[4] = signals[lengths.index(4)]
    keys[7] = signals[lengths.index(3)]
    keys[8] = signals[lengths.index(7)]
    for k in keys:
        if k is not None:
            signals.remove(k)

    for s in signals:
        if len(s) == 6:
            if set(keys[4]) <= set(s):
                keys[9] = s
            elif set(keys[7]) <= set(s):
                keys[0] = s
            else:
                keys[6] = s
        else:
            if set(keys[7]) <= set(s):
                keys[3] = s
            elif sum(x in set(keys[4]) for x in s) == 2:
                keys[2] = s
            else:
                keys[5] = s

    keys = [sorted(x) for x in keys]
    output = [sorted(x) for x in output]

    result += int("".join(str(keys.index(x)) for x in output))


print(result)
