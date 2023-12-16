import itertools


def main():
    start = "11110010111001001"
    print("part 1:", fill_disk(start, 272))
    print("part 2:", fill_disk(start, 35651584))


def fill_disk(s, length):
    while len(s) < length:
        s = s + "0" + "".join(["0" if c == "1" else "1" for c in s[::-1]])

    return checksum(s[:length])


def checksum(s):
    res = "".join(["1" if a == b else "0" for a, b in itertools.batched(s, 2)])
    if len(res) % 2 == 1:
        return res

    return checksum(res)


if __name__ == "__main__":
    main()
