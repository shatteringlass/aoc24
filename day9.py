DAY = 3
PARTS = [1, 2]


def parse_input():
    with open(f"day{DAY}.txt", "r") as fp:
        lines = fp.readlines()
    return lines

def part_one(lines):
    result = 0

    return result

def part_two(lines):
    result = 0

    return result


def main():
    lines = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(lines)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(lines)}")


if __name__ == "__main__":
    main()
