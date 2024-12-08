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


def step(position, direction, obstacles):
    next_position = tuple(sum(x) for x in zip(position, direction.value))
    while next_position in obstacles:
        # print(f"Met obstacle at {next_position}")
        direction = Direction((direction.value[1], -direction.value[0]))
        next_position = tuple(sum(x) for x in zip(position, direction.value))
    return next_position, direction


def walk_grid(rows, cols, start, obstacles, direction=Direction.N):
    seen = set()
    seen.add((start, Direction(direction.value)))
    sequence = list()
    pos = start

    while pos[0] >= 0 and pos[1] >= 0 and pos[0] < rows and pos[1] < cols:
        pos, direction = step(pos, direction, obstacles)
        if (pos, direction) in seen:
            return None
        else:
            seen.add((pos, direction))
            sequence.append(pos)

    return sequence


def print_grid(rows, cols, start, obstacles, visited):
    for r in range(rows):
        row = ''
        for c in range(cols):
            is_obstacle = False
            for obstacle in obstacles:
                if (r, c) == obstacle:
                    row += '#'
                    is_obstacle = True
                    break
            if not is_obstacle:
                if (r, c) == start:
                    row += '^'
                elif (r, c) in visited:
                    row += 'x'
                else:
                    row += '.'
        print(row)


def part_one(rows, cols, start, obstacles):

    steps = walk_grid(rows, cols, start, obstacles)
    #print_grid(rows, cols, start, obstacles, steps)

    return len(set(s for s in steps))


def part_two(rows, cols, start, obstacles):
    added_obstacles = set()

    path = walk_grid(rows, cols, start, obstacles)

    for tile in path:
        if tile != start:
            new_obstacles = obstacles.copy()
            new_obstacles.add(tile)
            revisited = walk_grid(rows, cols, start, new_obstacles)
            if not revisited:
                # print(f"Adding an obstacle at {tile} creates a loop!")
                added_obstacles.add(tile)
                #print_grid(rows, cols, start, new_obstacles, visited)
                # input()

    return len(added_obstacles)


def main():
    rows, cols, start, obstacles = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(rows, cols, start, obstacles)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(rows, cols, start, obstacles)}")


if __name__ == "__main__":
    main()
