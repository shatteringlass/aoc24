import enum

DAY = 4
PARTS = [1, 2]


class Direction(enum.Enum):
    W = (0, -1)
    E = (0, +1)
    N = (-1, 0)
    S = (1, 0)
    NE = (-1, 1)
    NW = (-1, -1)
    SE = (1, 1)
    SW = (1, - 1)


def move(position, direction):
    return tuple(position[i] + direction[i] for i, _ in enumerate(position))


def parse_input(chars, start):
    letters = {}
    starts = []
    with open(f"day{DAY}.txt", "r") as fp:
        for row, line in enumerate(fp.readlines()):
            for column, char in enumerate(line):
                if char in chars:
                    letters[(row, column)] = char
                if char == start:
                    starts.append((row, column))
    return letters, starts


def part_one(letters, starts):
    result = 0

    # for each X in the input
    for start in starts:
        # for each possible direction
        for direction in Direction:
            # set the required suffix
            word = 'MAS'
            # set the starting point
            pos = start + tuple()
            # iterate on the remaining characters in the suffix
            for step, letter in enumerate(word):
                # take a step
                pos = move(pos, direction.value)
                # check if landed on the right letter
                found = letters.get(pos, None)
                if letter != found:
                    # change direction if not
                    step -= 1
                    break

            # mark as found if all chars in the suffix were iterated
            if step == 2:
                result += 1

    return result


def part_two(letters, starts):
    result = 0
    directions = [(Direction.NW, Direction.SE), (Direction.NE, Direction.SW)]

    for start in starts:
        is_cross = True
        for (d1, d2) in directions:
            p1 = move(start, d1.value)
            p2 = move(start, d2.value)
            diagonal = letters.get(p1, '') + letters[start] + letters.get(p2, '') 
            if diagonal not in ('SAM', 'MAS'):
                is_cross = False
        if is_cross:
            result += 1

    return result


def main():
    for part in PARTS:
        if part == 1:
            letters, starts = parse_input("XMAS", "X")
            print(f"Result for part {part} is {part_one(letters, starts)}")
        elif part == 2:
            letters, starts = parse_input("MAS", "A")
            print(f"Result for part {part} is {part_two(letters, starts)}")


if __name__ == "__main__":
    main()
