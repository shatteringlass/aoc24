DAY = 7
PARTS = [1, 2]


def parse_input():
    equations = []
    with open(f"day{DAY}.txt", "r") as fp:
        for line in fp.readlines():
            p1, p2 = line.split(': ')
            equations.append((int(p1), list(int(x) for x in p2.split())))

    return equations


def test_equation(target, numbers, current=0, concat=False):

    if len(numbers) == 0:
        return target == current

    if current > target:
        return False

    return (
        test_equation(target, numbers[1:], current + numbers[0], concat=concat)
        or test_equation(target, numbers[1:], current*numbers[0], concat=concat)
        or (concat and test_equation(target, numbers[1:], int(str(current) + str(numbers[0])), concat=concat))
    )


def part_one(equations):
    result = 0

    for target, numbers in equations:
        if test_equation(target, numbers):
            result += target

    return result


def part_two(equations):
    result = 0

    for target, numbers in equations:
        if test_equation(target, numbers, concat=True):
            result += target

    return result


def main():
    equations = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(equations)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(equations)}")


if __name__ == "__main__":
    main()
