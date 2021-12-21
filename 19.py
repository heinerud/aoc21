import collections
import itertools
import math

rotations = [
    ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
    ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
    ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),
    ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
    ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
    ((0, -1, 0), (0, 0, -1), (1, 0, 0)),
    ((0, -1, 0), (0, 0, 1), (-1, 0, 0)),
    ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
    ((0, 0, -1), (-1, 0, 0), (0, 1, 0)),
    ((0, 0, -1), (0, -1, 0), (-1, 0, 0)),
    ((0, 0, -1), (0, 1, 0), (1, 0, 0)),
    ((0, 0, -1), (1, 0, 0), (0, -1, 0)),
    ((0, 0, 1), (-1, 0, 0), (0, -1, 0)),
    ((0, 0, 1), (0, -1, 0), (1, 0, 0)),
    ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
    ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
    ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
    ((0, 1, 0), (0, 0, -1), (-1, 0, 0)),
    ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
    ((0, 1, 0), (1, 0, 0), (0, 0, -1)),
    ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
    ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
    ((1, 0, 0), (0, 0, 1), (0, -1, 0)),
    ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
]


def rotate(beacons, r1, r2, r3):
    for b in beacons:
        x = sum(a * b for a, b in zip(b, r1))
        y = sum(a * b for a, b in zip(b, r2))
        z = sum(a * b for a, b in zip(b, r3))
        yield (x, y, z)


def manhattan(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))


def distance(p1, p2):
    return sum((a - b) * (a - b) for a, b in zip(p1, p2))


def min_offset(p1, p2):
    return min(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]), abs(p1[2] - p2[2]))


def max_offset(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]), abs(p1[2] - p2[2]))


def fingerprint(readings):
    fingerprints = {}
    for r1, r2 in itertools.combinations(readings, 2):
        id = (distance(r1, r2), min_offset(r1, r2), max_offset(r1, r2))
        assert id not in fingerprints
        fingerprints[id] = (r1, r2)

    return fingerprints


def match(s1, s2):
    fp1 = fingerprint(s1)
    fp2 = fingerprint(s2)
    common_ids = set(fp1).intersection(set(fp2))
    matches = collections.defaultdict(lambda: collections.Counter())
    for id in common_ids:
        b1, b2 = fp1[id]
        b3, b4 = fp2[id]
        matches[b1][b3] += 1
        matches[b1][b4] += 1
        matches[b2][b3] += 1
        matches[b2][b4] += 1

    return {k: max(v, key=v.get) for k, v in matches.items()}


def main():
    with open("./19.in") as f:
        input = f.read().split("\n\n")

    scans = []
    for s in input:
        readings = set()
        for b in s.splitlines()[1:]:
            x, y, z = b.split(",")
            readings.add((int(x), int(y), int(z)))
        scans.append(readings)

    scanners = set([(0, 0, 0)])
    max_scanner_distance = 0
    full_scan, *scans = scans
    while scans:
        for scan in scans:
            matches = match(full_scan, scan)
            if len(matches) < 12:
                continue

            for r in rotations:
                rotated_beacons = list(rotate(matches.values(), *r))
                match_distances = set(
                    distance(k, v) for k, v in zip(matches, rotated_beacons)
                )
                if len(match_distances) > 1:
                    continue

                scanner_position = tuple(
                    a - b for a, b in zip(list(matches.keys())[0], rotated_beacons[0])
                )
                scanners.add(scanner_position)
                for x, y, z in rotate(scan, *r):
                    full_scan.add(
                        (
                            x + scanner_position[0],
                            y + scanner_position[1],
                            z + scanner_position[2],
                        )
                    )
                break
            else:
                # We should always find a match
                assert False

            scans.remove(scan)
            break

    print(len(full_scan))
    assert len(full_scan) == 419

    max_distance = max(
        manhattan(p1, p2) for p1, p2 in itertools.combinations(scanners, 2)
    )
    print(max_distance)
    assert max_distance == 13210


if __name__ == "__main__":
    main()
