import hashlib


def main():
    passcode = "qzthpkfp"

    queue = [(passcode, 0, 0)]
    best = "x" * 1000
    longest = 0

    while queue:
        path, r, c = queue.pop()
        pathlen = len(path)
        if r == 3 and c == 3:
            if pathlen < len(best):
                best = path

            if pathlen > longest:
                longest = pathlen

            continue

        queue.extend(neighbors(path, r, c))

    print("part 1:", best.removeprefix(passcode))
    print("part 2:", longest - len(passcode))


def neighbors(path, row, col):
    u, d, l, r = hashlib.md5(path.encode()).hexdigest()[:4]

    ret = []

    if u in "bcdef" and 0 < row <= 3:
        ret.append((path + "U", row - 1, col))

    if d in "bcdef" and 0 <= row < 3:
        ret.append((path + "D", row + 1, col))

    if l in "bcdef" and 0 < col <= 3:
        ret.append((path + "L", row, col - 1))

    if r in "bcdef" and 0 <= col < 3:
        ret.append((path + "R", row, col + 1))

    return ret


if __name__ == "__main__":
    main()
