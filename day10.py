import enum
DAY = 10
PARTS = [1, 2]


class Direction(enum.Enum):
    W = (0, -1)
    E = (0, +1)
    N = (-1, 0)
    S = (1, 0)


def parse_input():
    tiles = {}
    with open(f"day{DAY}.txt", "r") as fp:
        for row, line in enumerate(fp):
            for col, char in enumerate(line.strip()):
                points = tiles.setdefault(int(char), set())
                points.add((row, col))
    return row+1, col+1, tiles


def next_valid_steps(tile, tiles, rows, cols):
    result = set()
    for d in Direction:
        height, row, col = tile
        step = tuple(sum(x) for x in zip((row, col), d.value))
        if step[0] >= 0 and step[0] < rows and step[1] >= 0 and step[1] < cols:
            if step and step in tiles[height+1]:
                result.add((height+1, *step))
    return result


def depth_first_search(start, tiles, rows, cols, skip_visited=True):
    paths = []
    visited = set()
    queue = [(start, [start, ])]

    while queue:
        current, path = queue.pop()

        if skip_visited:
            if current in visited:
                continue

            visited.add(current)

        if current[0] == 9:
            paths.append(path)
        else:
            queue.extend(
                (step, path + [step, ])
                for step in next_valid_steps(current, tiles, rows, cols)
            )

    return paths


def part_one(rows, cols, tiles):
    result = 0

    paths = {}

    for trailhead in tiles[0]:
        position = (0, *trailhead)
        paths[trailhead] = depth_first_search(position, tiles, rows, cols)

    return sum(len(p) for t, p in paths.items())


def part_two(rows, cols, tiles):
    result = 0

    paths = {}

    for trailhead in tiles[0]:
        position = (0, *trailhead)
        paths[trailhead] = depth_first_search(
            position, tiles, rows, cols, skip_visited=False)

    return sum(len(p) for t, p in paths.items())


def main():
    rows, cols, tiles = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(rows, cols, tiles)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(rows, cols, tiles)}")


if __name__ == "__main__":
    main()
