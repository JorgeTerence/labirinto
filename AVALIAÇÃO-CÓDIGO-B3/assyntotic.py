import sys

from main import Point, navigate


def _directions(_p):
    # Returns the 4 neighbors of a point
    # O(1)
    ...


def _bounded(_p):
    # Checks if a point is within the bounds of the map
    # O(1)
    ...


def _navigate(m, root, destiny, cur, path):
    ...

    for p in _directions(cur):  # O(1) ∵ it's a constant number of iterations
        if not p in path and _bounded(...):  # O(T_∆) ∵ p in track ∝ path size
            _ = navigate(m, root, destiny, p, path.copy())  # O(v) ∵ len(track) <= v
            ...

        # O(1)
        if p == destiny:
            ...

    else:
        ...


if __name__ == "__main__":
    if len(sys.argv) < 2:
        map_code = 1
    else:
        map_code = int(sys.argv[1])
    with open(f"./maps/{map_code:02d}.txt") as f:
        content = f.readlines()
        m = [[int(c) for c in line if c != "\n"] for line in content]

        start, end = [
            Point(x, y) for y, row in enumerate(m) for x, v in enumerate(row) if v == 2
        ]

        volume = len([v for row in m for v in row if v == 0])
        path = navigate(m, start, end)
        delta = len(path)

        print("Volume =", volume)
        print("∆ =", delta)
        print(str(path)[:56], "..." + "]")
