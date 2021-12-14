import collections

with open("14.in") as f:
    template, rules = f.read().split("\n\n")

rules = [x.split(" -> ") for x in rules.splitlines()]
rules = {pair: x for pair, x in rules}

pairs = (a + b for a, b in zip(template[:-1], template[1:]))
pairs = collections.Counter(pairs)

for i in range(1, 41):
    new_pairs = collections.Counter()
    for p, n in pairs.items():
        new_pairs[p[0] + rules[p]] += n
        new_pairs[rules[p] + p[1]] += n
    pairs = new_pairs

    if i in (10, 40):
        letters = collections.Counter()
        for p, n in pairs.items():
            letters[p[0]] += n
        letters[template[-1]] += 1
        print(max(letters.values()) - min(letters.values()))
