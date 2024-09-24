from typing import List, Tuple


# O(1)
def directions(p: Tuple[int, int]):
    return (p[0], p[1] - 1), (p[0], p[1] + 1), (p[0] - 1, p[1]), (p[0] + 1, p[1])


# O(1)
def bounded(p: Tuple[int, int], m: List[List[int]], h: int, w: int):
    return 0 <= p[0] < w and 0 <= p[1] < h and m[p[1]][p[0]] == 0


# O(n²)?
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
