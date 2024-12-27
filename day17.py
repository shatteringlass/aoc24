DAY = 17
PARTS = [1, 2]


class ThreeBitComputer:

    def __init__(self, registers):
        self.a, self.b, self.c = registers
        self.pointer = 0
        self._output = []
        self._opcodes = {
            0: self._adv,
            1: self._bxl,
            2: self._bst,
            3: self._jnz,
            4: self._bxc,
            5: self._out,
            6: self._bdv,
            7: self._cdv,
        }

    @property
    def output(self):
        return str(self._output)[1:-1].replace(" ", "")

    @property
    def opcodes(self):
        return self._opcodes

    def run(self, program):
        self.pointer = 0
        self._output = list()
        while True:
            if self.pointer // 2 >= len(program):
                break
            opcode, operand = program[self.pointer // 2]
            fun = self.opcodes[opcode]
            # input(f"###\nPointer: {self.pointer//2}\nOpcode: {opcode} ({fun.__name__})\nOperand: {operand}\nRegistry A: {self.a}\nRegistry B: {self.b}\nRegistry C: {self.c}")
            fun(operand)

    def fetch(self, operand):
        if operand < 4:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c

    def _adv(self, operand):
        # Opcode 0
        self.a = self.a // 2 ** self.fetch(operand)
        self.pointer += 2

    def _bxl(self, operand):
        # OPcode 1
        self.b ^= operand
        self.pointer += 2

    def _bst(self, operand):
        # OPcode 2
        self.b = self.fetch(operand) & 7
        self.pointer += 2

    def _jnz(self, operand):
        # OPCode 3
        if self.a:
            self.pointer = operand
        else:
            self.pointer += 2

    def _bxc(self, operand):
        # OPCode 4
        self.b ^= self.c
        self.pointer += 2

    def _out(self, operand):
        # OPCode 5 (write the last 3 bits of the operand to the output)
        self._output.append(self.fetch(operand) & 7)
        self.pointer += 2

    def _bdv(self, operand):
        # Opcode 6
        self.b = self.a // 2 ** self.fetch(operand)
        self.pointer += 2

    def _cdv(self, operand):
        # Opcode 7
        self.c = self.a // 2 ** self.fetch(operand)
        self.pointer += 2


def parse_input():
    registers = []
    program = []
    with open(f"day{DAY}.txt", "r") as fp:
        for line in fp:
            if "Register" in line:
                registers.append(int(line.split()[2]))
            elif "Program" in line:
                program = list(
                    map(
                        lambda x: (int(x[0]), int(x[1])),
                        zip(*[iter(line.split()[1].replace(",", ""))] * 2),
                    )
                )

    return registers, program


def part_one(registers, program):
    tbc = ThreeBitComputer(registers)
    tbc.run(program)
    result = tbc.output

    return result


def part_two(registers, program):
    tbc = ThreeBitComputer(registers)
    a = 0
    ps = [subitem for item in program for subitem in item]

    for i in range(len(ps) - 1, -1 , -1):
        a <<= 3

        while True:
            tbc.a = a
            tbc.run(program)
            if tbc._output != ps[i:]:
                a += 1
            else:
                break

    return a


def main():
    registers, program = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(registers, program)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(registers, program)}")


if __name__ == "__main__":
    main()
