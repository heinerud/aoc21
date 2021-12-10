with open("10.in") as f:
    lines = [x.strip() for x in f.readlines()]

opening = "({[<"
closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
errors = ""
autocomplete = []
for l in lines:
    expecting = []
    for x in l:
        if x in opening:
            expecting.append(closing[x])
        else:
            e = expecting.pop()
            if x != e:
                errors += x
                break
    else:
        autocomplete.append(reversed(expecting))


score = (
    errors.count(")") * 3
    + errors.count("]") * 57
    + errors.count("}") * 1197
    + errors.count(">") * 25137
)
print(score)

scores = []
for a in autocomplete:
    score = 0
    for x in a:
        score *= 5
        score += " )]}>".index(x)

    scores.append(score)

print(sorted(scores)[len(scores) // 2])
