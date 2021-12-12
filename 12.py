import collections

with open("12.in") as f:
    input = [x.strip().split("-") for x in f.readlines()]

graph = collections.defaultdict(list)
for a, b in input:
    if a == "end" or b == "start":
        a, b = b, a

    graph[a].append(b)

    if a != "start" and b != "end":
        graph[b].append(a)


def search_1(graph, path, paths=None):
    if paths is None:
        paths = []
    current = path[-1]
    if current in graph:
        for child in graph[current]:
            if child in path and child.islower():
                continue
            paths = search_1(graph, path + [child], paths)
    elif current == "end":
        paths += [path]
    return paths


def search_2(graph, path, double_visit, paths=None):
    if paths is None:
        paths = []
    current = path[-1]
    if current in graph:
        for child in graph[current]:
            if child != double_visit and child in path and child.islower():
                continue
            if child == double_visit and path.count(double_visit) > 1:
                continue
            paths = search_2(graph, path + [child], double_visit, paths)
    elif current == "end":
        paths += [path]
    return paths


# Part 1
print(len(search_1(graph, ["start"])))


# Part 2
lowercase = set()
for children in graph.values():
    lowercase.update(children)
lowercase.remove("end")

paths = set()
for x in lowercase:
    paths.update(" ".join(x) for x in search_2(graph, ["start"], x))
print(len(paths))
