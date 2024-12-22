DAY = 14
PARTS = [1, 2]

GRID_WIDTH = 101
GRID_HEIGHT = 103
SECONDS = 100


def move(start, speed, time):
    start_x, start_y = start
    speed_x, speed_y = speed
    return ((start_x + speed_x*time) % GRID_WIDTH, (start_y + speed_y*time) % GRID_HEIGHT)


def which_quadrant(position):
    pos_x, pos_y = position
    if pos_x == GRID_WIDTH // 2 or pos_y == GRID_HEIGHT // 2:
        return None
    else:
        return (int(pos_x > GRID_WIDTH // 2), int(pos_y > GRID_HEIGHT // 2))


def grid_safety(quadrants):
    safety = 1
    for quadrant in quadrants:
        if quadrant:
            safety *= quadrants[quadrant]
    return safety


def parse_input():
    robots = []
    with open(f"day{DAY}.txt", "r") as fp:
        for line in fp:
            robots.append(
                tuple(tuple(map(int, piece.split('=')[1].split(','))) for piece in line.split()))
    return robots


def part_one(robots):
    quadrants = {}

    for (position, speed) in robots:
        quadrant = which_quadrant(move(position, speed, SECONDS))
        try:
            quadrants[quadrant] += 1
        except KeyError:
            quadrants[quadrant] = 1

    print(quadrants)

    return grid_safety(quadrants)


def part_two(robots):
    result = 0

    return result


def main():
    robots = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(robots)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(robots)}")


if __name__ == "__main__":
    main()
