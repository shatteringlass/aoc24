import enum

from collections import deque
DAY = 12
PARTS = [1, 2]


class Direction(enum.Enum):
    W = (0, -1)
    E = (0, +1)
    N = (-1, 0)
    S = (1, 0)


def parse_input():
    cells = {}
    with open(f"day{DAY}.txt", "r") as fp:
        for row, line in enumerate(fp):
            for col, char in enumerate(line.strip()):
                cells[(row, col)] = char
    return cells


class Grid:
    def __init__(self, cells):
        self.cells = cells

    def find_regions(self):
        visited = set()

        for pos, char in self.cells.items():

            if pos in visited:
                continue

            region = set()
            plots = deque([pos])

            while plots:

                plot = plots.popleft()

                if plot in visited:
                    continue

                new_char = self.cells.get(plot, "")
                if new_char != char:
                    continue

                visited.add(plot)
                region.add(plot)

                for neighbor in self.neighbors(plot):
                    plots.append(neighbor)

            yield region

    def neighbors(self, point, inner_only=True):
        return [p for p in [tuple(sum(coord) for coord in zip(point, d.value)) for d in Direction] if (not(inner_only) or p in self.cells)]

    def get_perimeter(self, region):
        perimeter = 0
        for point in region:
            for neighbor in self.neighbors(point, inner_only=False):
                if neighbor not in region:
                    perimeter += 1
        return perimeter

    def count_sides(self, region):
        sides = 0
        for point in region:
            for neighbor in self.neighbors(point, inner_only=False):
                # TODO: figure out a proper way to count sides for a region
                pass
        return sides


def part_one(cells):
    result = 0
    g = Grid(cells)
    for r in g.find_regions():
        area = len(r)
        perimeter = g.get_perimeter(r)
        result += (area * perimeter)
    return result


def part_two(cells):
    result = 0
    g = Grid(cells)
    for r in g.find_regions():
        area = len(r)
        sides = g.count_sides(r)
        result += (area * sides)
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
