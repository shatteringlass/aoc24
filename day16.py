import enum
from heapq import heappop, heappush
DAY = 16
PARTS = [1, 2]


class Direction(enum.Enum):
    W = (0, -1)
    E = (0, +1)
    N = (-1, 0)
    S = (1, 0)


def parse_input():

    start = None
    end = None
    walls = set()

    with open(f"day{DAY}.txt", "r") as fp:
        row, col = 0, 0
        for line in fp:
            for char in line:
                if char == '\n':
                    col = 0
                    break
                elif char == 'E':
                    end = (row, col)
                elif char == 'S':
                    start = (row, col)
                elif char == '#':
                    walls.add((row, col))
                col += 1
            row += 1

    return start, end, walls, (row, col)


def search(start, end, walls, size):
    seen = set()
    queue = [(0, start, Direction.E.value)]
    rows, cols = size

    while queue:
        cost, *node = heappop(queue)
        node = tuple(node)
        #input(f"Current queue: {(node, cost)}")

        (x, y), (dx, dy) = node

        if (x, y) == end:
            return cost

        if node in seen:
            continue
        else:
            seen.add(node)

        for d in Direction:
            ndx, ndy = d.value
            #input(f"Checking in direction {ndx, ndy}")
            nx, ny = x + ndx, y + ndy
            if (nx, ny) in walls:
                continue
            elif not(nx in range(rows) and ny in range(cols)):
                continue
            else:
                weight = 1 if (ndx, ndy) == (dx, dy) else 1001
                heappush(queue, (cost+weight, (nx, ny), (ndx, ndy)))

    return None


def part_one(start, end, walls, size):
    #cost, path = search(start, end, walls, size)
    # return cost
    # assert (15,1) == start
    # assert (1,15) == end
    # assert (8,8) in walls
    # assert (17,17) == size
    return search(start, end, walls, size)


def part_two(start, end, walls, size):
    result = 0

    return result


def main():
    start, end, walls, size = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(start, end, walls, size)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(start, end, walls, size)}")


if __name__ == "__main__":
    main()
