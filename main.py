from typing import List, Tuple


RESET = "\033[0m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[35m"

colors = [GREEN, "", RESET]

# black = "\x1b[30m"
# blue = "\x1b[34m"
# magenta = "\x1b[35m"
# cyan = "\x1b[36m"
# white = "\x1b[37m"


def print_map(m):
    for row in m:
        for pos in row:
            print(colors[pos] + str(pos), RESET, end="")
        print("")


def print_track(m, track):
    for row in m:
        for pos in row:
            if pos in track:
                print(YELLOW + str(pos), RESET, end="")
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
    if len(track) > 12:
        print_track(m, track)
        print("-" * len(m[0]) * 2)
    for p in directions(cur):
        if p == destiny:
            print(track)
            track.append(p)
            return track

        if not p in track and bounded(p, m, h, w):
            navigate(m, root, destiny, p, track.copy())

    else:
        return 0


def bounded(p: Tuple[int, int], m: List[List[int]], h: int, w: int):
    return 0 <= p[0] < w and 0 <= p[1] < h and m[p[1]][p[0]] == 0


if __name__ == "__main__":
    with open("./maps/01.txt") as f:
        content = f.readlines()
        m = [[int(c) for c in list(line) if c != "\n"] for line in content]

        print_map(m)

        res = navigate(m, (0, 1), (9, 7), (0, 1), [])
        print(res)
