import enum
DAY = 15
PARTS = [1, 2]


class Direction(enum.Enum):
    W = (0, -1)
    E = (0, +1)
    N = (-1, 0)
    S = (1, 0)


class Maze:

    def __init__(self, walls, boxes, position):
        self.walls = walls
        self.boxes = boxes
        self.position = position

    @property
    def width(self):
        return max(self.walls, key=lambda x: x.position[1]).position[1]

    @property
    def height(self):
        return max(self.walls, key=lambda x: x.position[0]).position[0]

    def get_neighbor(self, tile, direction):
        return MazeObject(tuple(sum(x)
                         for x in zip(tile.position, direction.value)))

    def move(self, direction):
        neighbor = self.get_neighbor(self.position, direction)
        first_tile = neighbor.position
        if neighbor in self.walls:
            return self
        elif neighbor in self.boxes:
            #input(f"There is a box at {first_tile}, maybe it can be pushed")
            while (next_neighbor:=self.get_neighbor(neighbor, direction)) in self.boxes:
                #input(f"There is a box in direction {direction} w.r.t. {neighbor.position}")
                neighbor = next_neighbor
            if next_neighbor in self.walls:
                #input(f"Wall detected. Aborting move.")
                return self
            #input(f"Found a blank space at {next_neighbor}. The box at {first_tile} can be moved here.")
            self.boxes.remove(MazeObject(first_tile))
            self.boxes.add(next_neighbor)
        #input(f"Finally, the robot can advance from {self.position.position} to {first_tile}")
        self.position = Robot(first_tile)
        return self

    def print(self):
        for r in range(self.height+1):
            row = []
            for c in range(self.width+1):
                if MazeObject((r, c)) in self.walls:
                    row.append('#')
                elif MazeObject((r, c)) in self.boxes:
                    row.append('O')
                elif MazeObject((r, c)) == self.position:
                    row.append('@')
                else:
                    row.append('.')
            print(''.join(row))


class MazeObject:

    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position})"

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)


class Wall(MazeObject):
    pass


class Robot(MazeObject):
    pass


class Box(MazeObject):
    pass


def parse_input():
    walls = set()
    boxes = set()
    robot = None
    moves = []

    with open(f"day{DAY}.txt", "r") as fp:
        maze_l, moves_l = fp.read().split('\n\n')

        row = 0
        col = 0

        for char in maze_l:
            coord = (row, col)
            if char == '\n':
                row += 1
                col = 0
                continue
            elif char == '#':
                walls.add(coord)
            elif char == 'O':
                boxes.add(coord)
            elif char == '@':
                robot = coord
            col += 1

        for char in moves_l:
            if char == '^':
                moves.append(Direction.N)
            elif char == '>':
                moves.append(Direction.E)
            elif char == '<':
                moves.append(Direction.W)
            elif char == 'v':
                moves.append(Direction.S)

    return walls, boxes, robot,  moves


def part_one(walls, boxes, robot,  moves):
    result = 0

    maze = Maze(set(Wall(w) for w in walls), set(Box(b) for b in boxes), Robot(robot))

    # assert Wall((0, 0)) in maze.boxes
    # assert Box((1, 3)) in maze.boxes
    # assert Robot((24,24)) == maze.position

    for m in moves:
        maze = maze.move(m)
        #input()

    #maze.print()
        
    for b in maze.boxes:
        box_x, box_y = b.position
        result += box_x * 100 + box_y

    return result


def part_two(walls, boxes, robot,  moves):
    result = 0

    return result


def main():
    walls, boxes, robot,  moves = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(walls, boxes, robot,  moves)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(walls, boxes, robot,  moves)}")


if __name__ == "__main__":
    main()
