RESET = "\033[0m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"

# black = "\x1b[30m"
# yellow = "\x1b[33m"
# blue = "\x1b[34m"
# magenta = "\x1b[35m"
# cyan = "\x1b[36m"
# white = "\x1b[37m"


def print_map(m):
    for row in m:
        for pos in row:
            match pos:
                case 0:
                    print(GREEN + str(pos) + RESET, end=" ")
                case 1:
                    print(pos, end=" ")
                case 2:
                    print(RED + str(pos) + RESET, end=" ")

        print("")


if __name__ == "__main__":
    with open("./maps/01.txt") as f:
        content = f.readlines()
        m = [[int(c) for c in list(line) if c != "\n"] for line in content]
        print_map(m)
