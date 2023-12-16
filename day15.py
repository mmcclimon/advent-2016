from collections import namedtuple
import itertools


def main():
    Disk = namedtuple("Disk", ["id", "cycle", "start"])

    sample = [Disk(1, 5, 4), Disk(2, 2, 1)]
    _ = sample

    real = [
        Disk(1, 13, 1),
        Disk(2, 19, 10),
        Disk(3, 3, 2),
        Disk(4, 7, 1),
        Disk(5, 5, 3),
        Disk(6, 17, 5),
        # part 2
        Disk(7, 11, 0),
    ]

    p1 = 0
    for t in itertools.count():
        res = [at_time(d, t) for d in real]
        if not p1 and not any(res[:-1]):
            p1 = t
            print(f"part 1: {t}")

        if not any(res):
            print(f"part 2: {t}")
            break


def at_time(disk, t):
    return (t + disk.start + disk.id) % disk.cycle


if __name__ == "__main__":
    main()
