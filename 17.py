def step(p, v):
    p += v
    v -= 1 + 1j

    if v.real < 0:
        v = complex(0, v.imag)

    return p, v


def missed(p, v, right, bottom):
    if v.real > 0 and p.real > right:
        return True

    if v.imag < 0 and p.imag < bottom:
        return True

    return False


def hit(p, left, right, bottom, top):
    return left <= p.real <= right and bottom <= p.imag <= top


def shoot(p, v, left, right, bottom, top):
    apex = p.imag
    while not missed(p, v, right, bottom):
        if p.imag > apex:
            apex = p.imag

        if hit(p, left, right, bottom, top):
            return int(apex), True

        p, v = step(p, v)

    return int(apex), False


def main():
    with open("17.in") as f:
        input = f.read().strip()

    x, y = input.replace("target area: ", "").split(", ")
    xs = [int(x) for x in x.split("=")[1].split("..")]
    ys = [int(y) for y in y.split("=")[1].split("..")]
    left, right = min(xs), max(xs)
    bottom, top = min(ys), max(ys)

    p = 0 + 0j
    apex = p.imag
    hits = 0
    max_v_y = max(abs(top), abs(bottom))
    for x in range(max(abs(left), abs(right)) + 1):
        for y in range(-max_v_y - 1, max_v_y + 1):  # not sure about this
            height, is_hit = shoot(p, complex(x, y), left, right, bottom, top)
            if is_hit and height > apex:
                apex = height
            if is_hit:
                hits += 1

    print(apex)
    assert apex == 5050
    print(hits)
    assert hits == 2223


if __name__ == "__main__":
    main()
