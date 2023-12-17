def main():
    n = 3005290

    # solution to the Josephus problem from the Numberphile video, lol
    print("part 1:", int(f"{n:b}"[1:] + "1", 2))

    # Thes same thing, ish, but for powers of 3. (I needed some help here.)
    i = 1
    while i * 3 < n:
        i *= 3

    print("part 2:", n - i)


if __name__ == "__main__":
    main()
