DAY = 9
PARTS = [1, 2]


def parse_input():
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
    return sum(i*int(d) for i,d in enumerate(disk))

def part_one(disk):
    return checksum(compact(disk))


def part_two(disk):
    result = 0

    return result


def main():
    disk = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(disk)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(disk)}")


if __name__ == "__main__":
    main()
