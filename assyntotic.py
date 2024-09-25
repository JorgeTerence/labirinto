import sys
from math import hypot

from main import navigate


def _directions(_p):
    # Returns the 4 neighbors of a point
    # O(1)
    ...


def _bounded(_p):
    # Checks if a point is within the bounds of the map
    # O(1)
    ...


def _navigate(m, root, destiny, cur, track):
    track.append(cur)
    h, w = len(m), len(m[0])

    # O(1) because it's a constant number of iterations
    for p in _directions(cur):

        if (
            not p in track # O(T_∆)
            and
            _bounded(p, m, h, w)
        ):
            res = navigate(m, root, destiny, p, track.copy()) # O(v)
            if res:
                return res

        if p == destiny:
            track.append(p)
            return track

    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        map_code = 1
    else:
        map_code = int(sys.argv[1])
    with open(f"./maps/{map_code:02d}.txt") as f:
        content = f.readlines()
        m = [[int(c) for c in line if c != "\n"] for line in content]

        start, end = [
            (x, y) for y, row in enumerate(m) for x, v in enumerate(row) if v == 2
        ]

        delta = (abs(start[0] - end[0]), abs(start[1] - end[1]))
        print(f"∆x: {delta[0]}, ∆y: {delta[1]}")
        print(f"|∆|: {hypot(*delta):.2f}")

        zeroes = len([v for row in m for v in row if v == 0])
        print(f"Available spaces: {zeroes}")

        res = navigate(m, start, end, start, [])
        print(res)
