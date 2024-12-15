DAY = 9
PARTS = [1, 2]


def parse_input(part):
    if part == 1:
        return parse_input_p1()
    elif part == 2:
        return parse_input_p2()


def parse_input_p1():
    with open(f"day{DAY}.txt", "r") as fp:
        line = fp.read().strip()
        disk = [-1 for _ in range(len(line) * 9)]
        pos = 0
        for idx, char in enumerate(line):
            block_size = int(char)
            while block_size:
                if idx % 2 == 0:
                    disk[pos] = idx // 2
                block_size -= 1
                pos += 1
    return disk[:pos]


def parse_input_p2():
    with open(f"day{DAY}.txt", "r") as fp:
        pos = 0
        files, spaces = [], []
        for idx, char in enumerate(fp.read().strip()):
            size = int(char)
            blocks = (pos, size)
            if idx % 2 == 0:
                files.append(blocks)
            else:
                spaces.append(blocks)
            pos += size
    return files, spaces


def compact(disk):

    i, j = (0, len(disk) - 1)
    while i < j:
        while disk[i] != -1:
            i += 1
        while disk[j] == -1:
            j -= 1
        if i < j:
            disk[i] = disk[j]
            disk[j] = -1
        else:
            break

    return disk[:i]


def checksum(disk):
    return sum(i*int(d) for i, d in enumerate(disk))


def part_one(disk):
    return checksum(compact(disk))


def part_two(disk):
    result = 0

    files, spaces = disk

    for fidx in range(len(files) - 1, 1, -1):
        file_start, file_size = files[fidx]
        for sidx in range(len(spaces)):
            space_start, space_size = spaces[sidx]
            if (space_size and space_start < file_start and file_size <= space_size):
                files[fidx] = (space_start, file_size)
                spaces[sidx] = (space_start + file_size,
                                space_size - file_size)
                break

    files = sorted([(idx, start, size) for idx, (start, size)
                    in enumerate(files)], key=lambda x: x[1])

    i = 0
    s = []
    while files:
        file, *files = files
        for gap in range(file[1] - i):
            s.append('0')
            i += 1
        for rep in range(file[2]):
            s.append(str(file[0]))
            i += 1

    return checksum(s)


def main():
    for part in PARTS:
        disk = parse_input(part)
        if part == 1:
            print(f"Result for part {part} is {part_one(disk)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(disk)}")


if __name__ == "__main__":
    main()
