import functools

FAVORITE = 1350


def main():
    p1, p2 = search_for(31, 39)
    print("part 1:", p1)
    print("part 2:", p2)


@functools.cache
def is_wall(x, y):
    global FAVORITE
    result = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + FAVORITE
    return len(format(result, "b").replace("0", "")) % 2 == 1


# this is dijkstra's algorithm
def search_for(x, y):
    target = (x, y)
    cur = (1, 1)

    dists = {}
    seen = set()
    todo = set()

    dists[cur] = 0
    todo.add(cur)

    def get_dist(el):
        return dists[el]

    while True:
        cur = sorted(todo, key=get_dist)[0]
        todo.remove(cur)

        for node in neighbors(cur):
            if node not in dists:
                dists[node] = dists[cur] + 1
            else:
                dists[node] = min(dists[node], dists[cur] + 1)

            if node not in seen:
                todo.add(node)

        seen.add(cur)

        if target in todo:
            break

    smol = {xy for xy, dist in dists.items() if dist <= 50}

    return dists[target], len(smol)


def neighbors(coords):
    x, y = coords
    neighbs = []

    for x1, y1 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if x1 < 0 or y1 < 0:
            continue

        if not is_wall(x1, y1):
            neighbs.append((x1, y1))

    return neighbs


if __name__ == "__main__":
    main()
