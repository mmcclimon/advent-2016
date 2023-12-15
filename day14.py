from collections import defaultdict
import hashlib
import functools
import itertools
import re


def main():
    print(go(hash))
    print(go(hash_hard))


def go(hashfunc):
    three = re.compile(r"(.)\1{2}")
    keys = 0

    for i in itertools.count():
        md5 = hashfunc(i)

        if m := three.search(md5):
            want = m.group()[0] * 5
            for j in range(1, 1000):
                h = hashfunc(i + j)
                if want in h:
                    keys += 1
                    break

        if keys >= 64:
            return i


@functools.cache
def hash(n):
    salt = "ngcjuoqr"
    s = salt + str(n)
    return hashlib.md5(s.encode()).hexdigest()


@functools.cache
def hash_hard(n):
    # salt = "abc"
    salt = "ngcjuoqr"
    s = salt + str(n)

    for i in range(2017):
        s = hashlib.md5(s.encode()).hexdigest()

    return s


if __name__ == "__main__":
    main()
