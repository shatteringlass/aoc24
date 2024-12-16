DAY = 12
PARTS = [1, 2]


def parse_input():
    cells = {}
    with open(f"day{DAY}.txt", "r") as fp:
        for row, line in enumerate(fp):
            for col, char in enumerate(line.strip()):
                cells[(row, col)] = char
    return cells


def find_regions(cells):
    region = set()
    yield region


def get_perimeter(region):
    return None


def part_one(cells):
    result = 0

    print(cells)

    return result


def part_two(cells):
    result = 0

    return result


def main():
    cells = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(cells)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(cells)}")


if __name__ == "__main__":
    main()
