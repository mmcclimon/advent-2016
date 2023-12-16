def main():
    start = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
    print(gen_grid(start, 40))
    print(gen_grid(start, 400000))


def gen_grid(start, rows):
    grid = [start]
    for i in range(rows - 1):
        above = grid[i]
        buf = []

        for j in range(len(above)):
            l = above[j - 1] if j > 0 else "."
            c = above[j]
            r = above[j + 1] if j + 1 < len(above) else "."
            s = l + c + r

            if s in ["^^.", ".^^", "^..", "..^"]:
                buf.append("^")
            else:
                buf.append(".")

        grid.append("".join(buf))

    return sum(1 for line in grid for char in line if char == ".")


if __name__ == "__main__":
    main()
