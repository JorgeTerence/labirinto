from typing import List, Tuple
import sys

RESET = "\033[0m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[93m"

colors = [GREEN, "", RED]


def print_map(m):
    for row in m:
        for pos in row:
            print(colors[pos] + str(pos), RESET, end="")
        print("")


def print_track(m, track):
    for i, row in enumerate(m):
        for j, pos in enumerate(row):
            if pos == 2:
                print(YELLOW + "#", RESET, end="")
            elif (j, i) in track:
                print(RED + "@", RESET, end="")
            else:
                print(colors[pos] + str(pos), RESET, end="")
        print("")


def directions(p):
    return (p[0], p[1] - 1), (p[0], p[1] + 1), (p[0] - 1, p[1]), (p[0] + 1, p[1])


def navigate(
    m: List[List[int]],
    root: Tuple[int, int],
    destiny: Tuple[int, int],
    cur: Tuple[int, int],
    track: List,
):
    track.append(cur)
    h, w = len(m), len(m[0])

    for p in directions(cur):
        if p == destiny:
            track.append(p)
            return track

        if not p in track and bounded(p, m, h, w):
            res = navigate(m, root, destiny, p, track.copy())
            if res:
                return res

    else:
        return False


def bounded(p: Tuple[int, int], m: List[List[int]], h: int, w: int):
    return 0 <= p[0] < w and 0 <= p[1] < h and m[p[1]][p[0]] == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        map_code = 1
    else:
        map_code = int(sys.argv[1])
    with open(f"./maps/{map_code:02d}.txt") as f:
        content = f.readlines()
        m = [[int(c) for c in list(line) if c != "\n"] for line in content]

        print_map(m)

        print("-" * (2 * len(m[0]) - 1))

        start, end = [
            (x, y) for y, row in enumerate(m) for x, v in enumerate(row) if v == 2
        ]

        res = navigate(m, start, end, start, [])
        if res == 0:
            print("num deu :(")
        else:
            print_track(m, res)
