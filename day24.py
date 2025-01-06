DAY = 24
PARTS = [1, 2]

import operator

gate_dict = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}


def parse_input():
    wires = {}
    gates = {}

    read_gates = False

    with open(f"day{DAY}.txt", "r") as fp:
        for line in fp:
            if read_gates:
                i1, op, i2, _, out = line.strip().split()
                gates[out] = (gate_dict[op], (i1, i2))
            elif line == "\n":
                read_gates = True
                continue
            else:
                i, l = line.strip().split(": ")
                wires[i] = bool(int(l))

    return wires, gates


def part_one(wires, gates):
    result = 0

    all_gates = set(w for w in gates)
    remaining = set(w for w in all_gates if w.startswith("z"))

    while remaining:
        # until all z output wires have been evaluated, pick a random output wire
        wire = all_gates.pop()
        # fetch its input gate
        op, inputs = gates[wire]
        try:
            # try to sense its inputs
            new_inputs = tuple(wires[i] for i in inputs)
        except KeyError:
            # some input value not yet available
            all_gates.add(wire)
            continue
        else:
            # compute the result
            wires[wire] = op(*new_inputs)
            if wire.startswith("z"):
                remaining.remove(wire)

    pwr = 0

    for k, v in sorted(wires.items()):
        if k.startswith("z"):
            result += v * (2**pwr)
            pwr += 1

    return result


def part_two(wires, gates):
    result = 0

    return result


def main():
    wires, gates = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(wires, gates)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(wires, gates)}")


if __name__ == "__main__":
    main()
