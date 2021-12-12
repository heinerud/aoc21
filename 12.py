import collections

with open("12.in") as f:
    input = [x.strip().split("-") for x in f.readlines()]

graph = collections.defaultdict(set)
for a, b in input:
    if a == "end" or b == "start":
        a, b = b, a

    graph[a].add(b)

    if a != "start" and b != "end":
        graph[b].add(a)


def search(graph, start, part2):
    paths = 0
    q = collections.deque([(start, set(), False)])
    while q:
        current, visited_small, twice = q.popleft()
        if current == "end":
            paths += 1
            continue
        for child in graph[current]:
            if child not in visited_small:
                new_visited_small = set(visited_small)
                if child.islower():
                    new_visited_small.add(child)
                q.append((child, new_visited_small, twice))
            elif part2 and not twice:
                q.append((child, visited_small, True))
    return paths


print(search(graph, "start", False))
print(search(graph, "start", True))
