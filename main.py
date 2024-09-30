import sys
from dataclasses import dataclass

RESET = "\033[0m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[93m"

colors = ["", GREEN, RED]


@dataclass
class Point:
    """x y coordinate"""

    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"

    def is_neighbor(self, other) -> bool:
        return abs(self.x - other.x) + abs(self.y - other.y) == 1

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def print_map(m: list[list[int]]) -> None:
    for row in m:
        for pos in row:
            print(colors[pos] + str(pos), RESET, end="")
        print("")


def print_track(m: list[list[int]], path: list[Point]) -> None:
    for y, row in enumerate(m):
        for x, cell in enumerate(row):
            if cell == 2:
                print(RED + "#", RESET, end="")
            elif Point(x, y) in path:
                print(YELLOW + "@", RESET, end="")
            else:
                print(colors[cell] + str(cell), RESET, end="")
        print("")


def directions(p: Point) -> tuple[Point, Point, Point, Point]:
    return (
        Point(p.x, p.y - 1),
        Point(p.x, p.y + 1),
        Point(p.x - 1, p.y),
        Point(p.x + 1, p.y),
    )


def bounded(p: Point, m: list[list[int]], h: int, w: int) -> bool:
    return 0 <= p.x < w and 0 <= p.y < h and m[p.y][p.x] == 0


def navigate(
    m: list[list[int]],
    root: Point,
    destiny: Point,
    cur: Point = None,
    path: list[Point] = [],
) -> list[Point] | bool:
    if cur is None:
        cur = root

    path.append(cur)
    h, w = len(m), len(m[0])

    for p in directions(cur):
        if not p in path and bounded(p, m, h, w):
            if res := navigate(m, root, destiny, p, path.copy()):
                return res

        if p == destiny:
            path.append(p)
            return path

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

        print_map(m)
        print("-" * (2 * len(m[0]) - 1))

        start, end = [
            Point(x, y) for y, row in enumerate(m) for x, v in enumerate(row) if v == 2
        ]

        path = navigate(m, start, end)

        if not path:
            print("num deu :(")
        else:
            print_track(m, path)
            print(path)
