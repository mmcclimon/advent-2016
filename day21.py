import itertools
import re


def main():
    file = "input21.txt"

    with open(file) as f:
        lines = [line.strip() for line in f]

    print("part 1:", scramble(lines, "abcdefgh"))

    # lol, weak password is weak. Just brute-force it, it's fine.
    target = "fbgdceah"
    for candidate in itertools.permutations("abcdefgh"):
        if scramble(lines, candidate) == target:
            print("part 2:", "".join(candidate))
            break


def scramble(lines, word):
    for line in lines:
        word = process_line(line, word)

    return word


def process_line(line, word):
    s = list(word)

    def swap_idx(a, b):
        s[a], s[b] = s[b], s[a]
        return "".join(s)

    def rotate_right(n):
        nonlocal s
        for _ in range(n):
            s = [s[-1]] + s[:-1]
        return "".join(s)

    def rotate_left(n):
        nonlocal s
        for _ in range(n):
            s = s[1:] + [s[0]]
        return "".join(s)

    if m := re.match(r"swap position (\d) with position (\d)", line):
        a, b = [int(g) for g in m.groups()]
        return swap_idx(a, b)

    if m := re.match(r"swap letter (.) with letter (.)", line):
        a, b = [s.index(g) for g in m.groups()]
        return swap_idx(a, b)

    if m := re.match(r"rotate (left|right) (\d) step", line):
        n = int(m.group(2))
        return rotate_left(n) if m.group(1) == "left" else rotate_right(n)

    if m := re.match(r"rotate based on position of letter (.)", line):
        idx = s.index(m.group(1))
        return rotate_right(1 + idx + (1 if idx >= 4 else 0))

    if m := re.match(r"reverse positions (\d) through (\d)", line):
        a, b = [int(g) for g in m.groups()]
        b += 1
        return "".join(s[0:a] + list(reversed(s[a:b])) + s[b:])

    if m := re.match(r"move position (\d) to position (\d)", line):
        a, b = [int(g) for g in m.groups()]
        char = s[a]
        del s[a]
        s.insert(b, char)
        return "".join(s)

    raise RuntimeError(f"bogus line: {line}")


if __name__ == "__main__":
    main()
