import math


def main():
    file = "input25.txt"
    with open(file) as f:
        lines = [line.strip() for line in f]

    print(go(lines, 158))


# This function was very useful for determining what the assembly actually does.
def go(lines, a):
    cpu = {"a": a, "b": 0, "c": 0, "d": 0}
    ip = 0

    def resolve(val):
        try:
            return int(val)
        except ValueError:
            return cpu[val]

    outs = 0

    while True:
        if ip >= len(lines):
            break

        # if ip == 28 and cpu["a"] == 0:
        #     print("a is 0?!")
        #     print(cpu)
        #     break

        instr = lines[ip]
        cached = ip
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

            case "out":
                reg = rest[0]
                print(f"OUT: {resolve(reg)}")
                print(cpu)
                outs += 1
                if outs == 25:
                    break

            case _:
                raise RuntimeError("bad instruction: " + instr)

        ip += 1
        # print(f"after {cached:2} {instr + ":":10} {cpu}")

    # return cpu["a"]


if __name__ == "__main__":
    main()
