DAY = 1
PARTS = [1, 2]


def parse_input():
    with open(f"day{DAY}.txt", "r") as fp:
        lines = fp.readlines()
    return lines


def part_one():
    result = 0
    lines = parse_input()
    left, right = [sorted([row.split()[col] for row in lines]) for col in (0, -1)]

    for pair_idx in range(len(lines)):
        result += abs(int(left[pair_idx]) - int(right[pair_idx]))

    return result


def part_two():
    result = 0
    lines = parse_input()
    left, right = [[int(row.split()[col]) for row in lines] for col in (0, -1)]

    seen = {}

    for item in left:
        if item in seen:
            continue
        else:
            seen[item] = sum(1 for x in right if x == item)
        result += item * seen[item]
    
    return result


def main():
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one()}")
        elif part == 2:
            print(f"Result for part {part} is {part_two()}")


if __name__ == "__main__":
    main()
