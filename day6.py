import enum
DAY = 6
PARTS = [1, 2]


class Direction(enum.Enum):
    W = (0, -1)
    E = (0, +1)
    N = (-1, 0)
    S = (1, 0)


def parse_input():
    obstacles = set()
    with open(f"day{DAY}.txt", "r") as fp:
        for row, line in enumerate(fp):
            for col, char in enumerate(line):
                if char == '^':
                    start = (row, col)
                if char == '#':
                    obstacles.add((row, col))
    return row+1, col+1, start, obstacles


def walk(position, direction, obstacles):
    next_position = tuple(sum(x) for x in zip(position, direction.value))
    if next_position in obstacles:
        direction = Direction((direction.value[1], -direction.value[0]))
        print(f"Heading {direction} now")
        return tuple(sum(x) for x in zip(position, direction.value)), direction
    return next_position, direction


def part_one(rows, cols, start, obstacles):
    result = 0
    seen = set()
    pos = start
    seen.add(pos)
    print(f"The grid has {rows} rows and {cols} cols")
    print(f"Starting at {pos}")
    direction = Direction.N

    while pos[0] >= 0 and pos[1] >= 0 and pos[0] < rows and pos[1] < cols:
        print(f"Currently at {pos} heading {direction}")
        pos, direction = walk(pos, direction, obstacles)
        if pos in seen:
            continue
        else:
            seen.add(pos)
            result += 1

    return result


def part_two(rows, cols, start, obstacles):
    result = 0

    return result


def main():
    rows, cols, start, obstacles = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(rows, cols, start, obstacles)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(rows, cols, start, obstacles)}")


if __name__ == "__main__":
    main()
