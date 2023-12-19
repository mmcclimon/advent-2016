import itertools
import math


def main():
    file = "input24.txt"
    # file = "t.txt"

    grid = set()
    numbers = {}

    with open(file) as f:
        for r, line in enumerate(f):
            for c, char in enumerate(line.strip()):
                if char.isdigit():
                    numbers[char] = (r, c)

                if char != "#":
                    grid.add((r, c))

    p1, p2 = go(grid, numbers)
    print("part 1:", p1)
    print("part 2:", p2)


def go(grid, numbers):
    # Generate shortest paths starting from all individual numbers
    froms = {}
    for n, pos in numbers.items():
        froms[n] = dists_from(grid, pos)

    # Now, check all permutations of orders, not counting 0. (This is
    # obviously bogus, but we can do it because n is small, and checking 5k
    # perms is no big deal.)
    del numbers["0"]
    keys = sorted(numbers)

    p1 = p2 = math.inf

    for p in itertools.permutations(keys):
        dist = froms["0"][numbers[p[0]]]  # must start from 0

        for i in range(len(p) - 1):
            # Get dist from p[i] to the location of p[i+1]
            dist += froms[p[i]][numbers[p[i + 1]]]

        p1 = min(p1, dist)

        # For part 2, must also return to 0
        dist += froms["0"][numbers[p[-1]]]
        p2 = min(p2, dist)

    return p1, p2


def dists_from(grid, start):
    dists = {}
    seen = set()
    todo = set()

    dists[start] = 0
    todo.add(start)

    def neighbors(r, c):
        return [
            (r1, c1)
            for r1, c1 in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            if (r1, c1) in grid
        ]

    def get_dist(node):
        return dists[node]

    while todo:
        cur = sorted(todo, key=get_dist)[0]
        todo.remove(cur)

        for node in neighbors(*cur):
            if node not in dists:
                dists[node] = dists[cur] + 1
            else:
                dists[node] = min(dists[node], dists[cur] + 1)

            if node not in seen:
                todo.add(node)

        seen.add(cur)

    return dists


if __name__ == "__main__":
    main()
