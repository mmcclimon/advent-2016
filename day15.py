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
        Disk(7, 11, 0),  # for part 2
    ]

    cycles = [0] * (len(real) + 1)
    inc = 1

    for i, disk in enumerate(real):
        for t in itertools.count(cycles[i], inc):
            if (t + disk.start + disk.id) % disk.cycle == 0:
                cycles[i + 1] = t
                inc *= disk.cycle
                break

    print("part 1:", cycles[6])
    print("part 2:", cycles[7])


if __name__ == "__main__":
    main()
