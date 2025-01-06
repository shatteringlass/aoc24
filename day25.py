DAY = 25
PARTS = [1, 2]


def parse_block(block):
    if block[0].startswith("#"):
        # lock (top-down)
        return 1, parse_lock(block)
    else:
        # key (bottom-up)
        return 0, parse_key(block)


def parse_lock(block):
    counter = dict()
    for row_idx in range(1, len(block)):
        for col_idx in range(len(block[row_idx])):
            if col_idx not in counter:
                counter[col_idx] = 0
            counter[col_idx] += int(block[row_idx][col_idx] == "#")
    return tuple(counter.values())


def parse_key(block):
    return parse_lock(block[::-1])


def check_key(key, lock):
    for k, l in zip(key, lock):
        if k + l > 5:
            return False
    return True


def parse_input():
    keys = list()
    locks = list()

    with open(f"day{DAY}.txt", "r") as fp:
        for b in fp.read().split("\n\n"):
            block_type, heights = parse_block(b.split())
            (keys, locks)[block_type].append(heights)

    return keys, locks


def part_one(keys, locks):
    result = 0

    for key in keys:
        for lock in locks:
            if check_key(key, lock):
                result += 1

    return result


def part_two(keys, locks):
    result = 0

    return result


def main():
    keys, locks = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(keys, locks)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(keys, locks)}")


if __name__ == "__main__":
    main()
