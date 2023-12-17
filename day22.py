import re


def main():
    file = "input22.txt"
    # file = "t.txt"

    with open(file) as f:
        lines = [line.strip() for line in f]

    disks = []

    for line in lines[2:]:
        disks.append(Disk(line))

    grid = {}

    # part 1
    pairs = 0
    for a in disks:
        grid[a.x, a.y] = a
        for b in disks:
            if a.used and a != b and a.used <= b.avail:
                pairs += 1

    print(pairs)

    # This code just prints the grid, at which point it's fairly trivial to
    # solve by hand.

    max_x = max(d.x for d in disks)
    max_y = max(d.y for d in disks)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            d = grid[x, y]
            if d.used > 400:
                print("#", end="")
            else:
                print("_" if d.used == 0 else ".", end="")

        print("")


class Disk:
    def __init__(self, line):
        dev, size, used, avail, pct = line.split()
        self.dev = dev
        self.size = int(size.removesuffix("T"))
        self.used = int(used.removesuffix("T"))
        self.avail = int(avail.removesuffix("T"))
        self.pct = int(pct.removesuffix("%"))

        m = re.search(r"x(\d+)-y(\d+)$", dev)
        assert m is not None
        self.x = int(m.group(1))
        self.y = int(m.group(2))

    def __repr__(self):
        return f"<Disk {self.x},{self.y} {self.used}/{self.size}>"


if __name__ == "__main__":
    main()


# /dev/grid/node-x0-y0     94T   72T    22T   76%
# /dev/grid/node-x36-y0    87T   72T    15T   82%
