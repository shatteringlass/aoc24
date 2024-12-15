DAY = 11
PARTS = [1, 2]


def change(stone):
    if stone == 0:
        yield 1
    elif len(txt:=str(stone)) % 2 == 0:
        yield int(txt[:len(txt)//2])
        yield int(txt[len(txt)//2:])
    else:
        yield stone*2024


def parse_input():
    stones = {}
    with open(f"day{DAY}.txt", "r") as fp:
        for x in fp.read().strip().split():
            if int(x) in stones:
                stones[int(x)] += 1
            else:
                stones[int(x)] = 1
    return stones


def blink(stones, times):
    for blink in range(times):
        new_stones = dict()
        for stone, count in stones.items():
            for chg in change(stone):
                if chg in new_stones:
                    new_stones[chg] += count
                else:
                    new_stones[chg] = count
        stones = new_stones

    return stones


def part_one(stones):
    stones = blink(stones, 25)
    return sum(stones.values())


def part_two(stones):
    stones = blink(stones, 75)
    return sum(stones.values())


def main():
    stones = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(stones)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(stones)}")


if __name__ == "__main__":
    main()
