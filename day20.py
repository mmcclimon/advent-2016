def main():
    biggest = 4_294_967_295

    with open("input20.txt") as f:
        raw = sorted(Range(line) for line in f)

    ranges = collapse_ranges(raw)

    print("part 1:", ranges[0].end + 1)

    # part 2
    count = 0

    for i in range(len(ranges) - 1):
        left, right = ranges[i], ranges[i + 1]
        count += right.start - left.end - 1

    assert ranges[-1].end >= biggest  # ensure we don't have extra ones at the end

    print("part 2:", count)


def collapse_ranges(raw):
    # collapse ranges as possible
    ranges = []
    prev = raw[0]

    for cur in raw[1:]:
        if prev.end + 1 < cur.start:
            ranges.append(prev)
            prev = cur
            continue

        prev.end = max(prev.end, cur.end)

    ranges.append(prev)
    return ranges


class Range:
    def __init__(self, line):
        l, r = line.strip().split("-")
        self.start = int(l)
        self.end = int(r)

    def __repr__(self):
        return f"<{self.start}-{self.end}>"

    def __lt__(self, other):
        return self.start < other.start


if __name__ == "__main__":
    main()
