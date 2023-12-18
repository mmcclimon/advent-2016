import math


def main():
    # file = "input23.txt"
    # with open(file) as f:
    #     lines = [line.strip() for line in f]

    # print(go(lines, 7))

    print("part 1:", answer(7))
    print("part 2:", answer(12))


def answer(a):
    return math.factorial(a) + (94 * 82)


# This function was very useful for determining what the assembly actually does.
def go(lines, a):
    return
    cpu = {"a": a, "b": 0, "c": 0, "d": 0}
    ip = 0

    def resolve(val):
        try:
            return int(val)
        except ValueError:
            return cpu[val]

    toggle = {
        "inc": "dec",
        "dec": "inc",
        "tgl": "inc",
        "cpy": "jnz",
        "jnz": "cpy",
    }

    while True:
        if ip >= len(lines):
            break

        instr = lines[ip]
        if instr == "tgl c":
            print(cpu)
        # print(f"{cpu} {ip:2} {instr}")
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
                    ip += resolve(offset)
                    ip -= 1  # we'll inc at the bottom of the loop

            case "tgl":
                val = resolve(rest[0])
                idx = ip + val
                if 0 <= idx < len(lines):
                    op, rest = lines[idx].split(" ", maxsplit=1)
                    lines[idx] = toggle[op] + " " + rest
                    print(f"  toggle {idx} ({op} {rest} -> {lines[idx]})")

            case _:
                raise RuntimeError("bad instruction: " + instr)

        ip += 1
        # print(f"  bottom of loop, {ip=}", cpu)

    return cpu["a"]


if __name__ == "__main__":
    main()
