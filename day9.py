DAY = 9
PARTS = [1, 2]


def parse_input():
    files, spaces = [], []
    with open(f"day{DAY}.txt", "r") as fp:
        for line in fp:
            for idx, char in enumerate(line):
                x = int(char)
                if idx % 2 == 0:
                    files.append((x, int(idx/2)))
                else:
                    spaces.append(x)
    return files, spaces

def part_one(files, spaces):
    result = 0

    input(files)

    reordered = [-1 for _ in range(len(files))]
    idx = len(files) - 1
    kdx = 0

    for jdx, space in enumerate(spaces):
        reordered[kdx] = files[jdx]
        while space:
            kdx += 1
            reordered[kdx] = files[idx]
            space -= 1
            while files[idx][0] > 0:
                files[idx] = (files[idx][0]-1, files[idx][1])
                idx -= 1

        print(kdx)

        if kdx == len(files) - 1:
            break

 #   while jdx < len(files):
 #       reordered[jdx] = files[]

    print(reordered)

    return result

def part_two(files, spaces):
    result = 0

    return result


def main():
    files, spaces = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(files, spaces)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(files, spaces)}")


if __name__ == "__main__":
    main()
