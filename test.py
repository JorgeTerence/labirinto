from main import navigate, print_track

if __name__ == "__main__":
    m1 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 0, 0, 0, 0, 0, 0, 0, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    track1 = navigate(m1, (0, 1), (8, 1), (0, 1), [])
    print_track(m1, track1)

    assert track1 != False, "There should be a path"
    assert (track1[0], track1[-1]) == ((0, 1), (8, 1)), "Start and destiny should be at [0,1] and [8,1]"
    assert track1 == [(i, 1) for i in range(9)], "Track should be complete"

    print("track1 passou nos testes")