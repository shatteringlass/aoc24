DAY = 8
PARTS = [1, 2]


def parse_input():
    antennas = dict()
    with open(f"day{DAY}.txt", "r") as fp:
        for i, line in enumerate(fp):
            for j, char in enumerate(line):
                if char != '.':
                    locations = antennas.setdefault(char, set())
                    locations.add((i, j))

    return i+1, j+1, antennas

def place_nodes(rows, cols, antennas, unlimited=False):
    nodes = set()
    for freq, coords in antennas.items():
        for (loc_x, loc_y) in coords:
            for (other_x, other_y) in coords:
                if (loc_x, loc_y) != (other_x, other_y):
                    # check along the line through these two points
                    distance = ((other_x - loc_x)**2+(other_y-loc_y)**2)**(1/2)
                    direction = ((other_x-loc_x)/distance, (other_y - loc_y)/distance)
                    k = 1 if unlimited else 2
                    while True:
                        x1 = loc_x+k*(other_x-loc_x)
                        y1 = loc_y+k*(other_y-loc_y)
                        if x1 >= 0 and x1 < rows and y1 >= 0 and y1 < cols:
                            nodes.add((x1,y1)) 
                        else:
                            break
                        if not unlimited:
                            break
                        else:
                            k += 1
                    k = 1 if unlimited else 2
                    while True:
                        x2 = other_x-k*(other_x-loc_x)
                        y2 = other_y-k*(other_y-loc_y)
                        if x2 >= 0 and x2 < rows and y2 >= 0 and y2 < cols:
                            nodes.add((x2,y2))
                        else:
                            break
                        if not unlimited:
                            break
                        else:
                            k += 1
    return nodes

def part_one(rows, cols, antennas):
    nodes = place_nodes(rows, cols, antennas)

    return len(nodes)


def part_two(rows, cols, antennas):
    nodes = place_nodes(rows, cols, antennas, unlimited=True)

    # for r in range(rows):
    #     row = ''
    #     for c in range(cols):
    #         has_antenna = False
    #         for freq, locs in antennas.items():
    #             if (r,c) in locs:
    #                 row += freq
    #                 has_antenna = True
    #                 break
    #         if not has_antenna:
    #             if (r,c) in nodes:
    #                 row += '#'
    #             else:
    #                 row += '.'
    #     print(row)

    return len(nodes)


def main():
    rows, cols, antennas = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(rows, cols, antennas)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(rows, cols, antennas)}")


if __name__ == "__main__":
    main()
