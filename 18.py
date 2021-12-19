import itertools
import math


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        if isinstance(self.value, int):
            return str(self.value)
        return f"[{str(self.left)},{str(self.right)}]"

    @property
    def has_leaves(self):
        return (
            self.left is not None
            and self.right is not None
            and self.left.value is not None
            and self.right.value is not None
        )

    @property
    def is_leaf(self):
        return self.value is not None


def parse(n):
    node = Node()
    if isinstance(n, int):
        node.value = n
        return node

    node.left = parse(n[0])
    node.right = parse(n[1])
    node.left.parent = node
    node.right.parent = node

    return node


def add(a, b):
    n = Node()
    n.left = a
    n.right = b
    n.left.parent = n
    n.right.parent = n
    return n


def magnitude(n):
    if isinstance(n.value, int):
        return n.value

    return 3 * magnitude(n.left) + 2 * magnitude(n.right)


def add_left(node):
    previous = node.left
    current = node
    while current is not None and (current.left == previous or current.left is None):
        previous, current = current, current.parent

    if current is not None:
        current = current.left
        while current.value is None:
            if current.right is not None:
                current = current.right
            else:
                current = current.left

        current.value += node.left.value


def add_right(node):
    previous = node.right
    current = node
    while current is not None and (current.right == previous or current.right is None):
        previous, current = current, current.parent

    if current is not None:
        current = current.right
        while current.value is None:
            if current.left is not None:
                current = current.left
            else:
                current = current.right

        current.value += node.right.value


def explode(root):
    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        if node is None:
            continue

        if depth == 4 and node.has_leaves:
            add_left(node)
            add_right(node)
            node.value = 0
            node.left = None
            node.right = None
            explode(root)

        stack.append((node.right, depth + 1))
        stack.append((node.left, depth + 1))


def split(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue

        if node.is_leaf and node.value >= 10:
            node.left = Node(math.floor(node.value / 2))
            node.right = Node(math.ceil(node.value / 2))
            node.left.parent = node
            node.right.parent = node
            node.value = None
            reduce(root)

        stack.append(node.right)
        stack.append(node.left)


def reduce(root):
    explode(root)
    split(root)
    return root


with open("./18.in") as f:
    lines = f.read().splitlines()
snailfish_numbers = [eval(l) for l in lines]

root = parse(snailfish_numbers[0])
for n in snailfish_numbers[1:]:
    root = reduce(add(root, parse(n)))

m = magnitude(root)
assert m == 3981
print(m)

max_magnitude = 0
for a, b in itertools.combinations(snailfish_numbers, 2):
    m1 = magnitude(reduce(add(parse(a), parse(b))))
    m2 = magnitude(reduce(add(parse(b), parse(a))))
    m = max(m1, m2)
    if m > max_magnitude:
        max_magnitude = m
assert max_magnitude == 4687
print(max_magnitude)
