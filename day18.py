import enum

DAY = 18
PARTS = [1, 2]

GRID_SIZE = 70


class Direction(enum.Enum):
    W = (0, -1)
    E = (0, +1)
    N = (-1, 0)
    S = (1, 0)


def valid_steps(position):
    x, y = position
    for d in Direction:
        dx, dy = d.value
        nx, ny = x + dx, y + dy
        if nx in range(GRID_SIZE) and ny in range(GRID_SIZE):
            yield (nx, ny)


def parse_input():
    falling_bytes = set()
    with open(f"day{DAY}.txt", "r") as fp:
        for line in fp:
            falling_bytes.add(tuple(map(int, (x for x in line.split(",")))))
    return falling_bytes


def part_one(falling_bytes):
    result = 0

    costs = dict()
    states = dict()
    queue = [(0, (0,0))]

    while queue:
        pass

    return result


def part_two(falling_bytes):
    result = 0

    return result


def main():
    falling_bytes = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(falling_bytes)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(falling_bytes)}")


if __name__ == "__main__":
    main()
