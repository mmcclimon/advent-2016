def main():
    file = "t.txt"
    file = "input12.txt"

    with open(file) as f:
        lines = [line.strip() for line in f]

    print("part 1:", go(lines, 0, 0, 0, 0))
    print("part 2:", go(lines, 0, 0, 1, 0))


def go(lines, a, b, c, d):
    cpu = {"a": a, "b": b, "c": c, "d": d}
    ip = 0

    def resolve(val):
        if val.isdigit():
            return int(val)

        return cpu[val]

    while True:
        if ip >= len(lines):
            break

        instr = lines[ip]
        # print(instr, cpu)
        op, *rest = instr.split()

        match op:
            case "cpy":
                val, reg = rest
                cpu[reg] = resolve(val)

            case "inc":
                reg = rest[0]
                cpu[reg] += 1

            case "dec":
                reg = rest[0]
                cpu[reg] -= 1

            case "jnz":
                reg, offset = rest
                if resolve(reg) != 0:
                    ip += int(offset)
                    ip -= 1  # we'll inc at the bottom of the loop

            case _:
                raise RuntimeError("bad instruction: " + instr)

        ip += 1

    return cpu["a"]


if __name__ == "__main__":
    main()
