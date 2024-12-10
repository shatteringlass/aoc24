DAY = 9
PARTS = [1, 2]


def parse_input():
    files, spaces = [], []
    with open(f"day{DAY}.txt", "r") as fp:
        for line in fp:
            for idx, char in enumerate(line):
                x = int(char)
                if idx % 2 == 0:
                    files.append((int(idx / 2), x))
                else:
                    spaces.append((int(idx / 2) + 1, x))
    return files, spaces


def defrag(files, spaces):

    if not spaces or not files:
        return []

    pos, width = spaces[0]
    file_id, blocks = files[-1]

    if width == blocks:
        prefix = [files[0], (file_id, width)]
        new_files = files[1:-1]
        new_spaces = spaces[1:]
    elif width < blocks:
        # not enough space, split in two
        prefix = [files[0], (file_id, width)]
        new_files = files[1:-1] + [(file_id, blocks - width)]
        new_spaces = spaces[1:]
    elif width > blocks:
        # leftover free space
        prefix = [files[0], (file_id, blocks)]
        new_files = files[1:-1]
        new_spaces = [(pos, width - blocks)] + spaces[1:]
    return prefix + defrag(new_files, new_spaces)


def part_one(files, spaces):
    result = 0

    reordered = defrag(files, spaces)

    print(''.join([str(s)*n for (s,n) in reordered]))

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
