DAY = 3
PARTS = [1, 2]

import re


def parse_input():
    with open(f"day{DAY}.txt", "r") as fp:
        text = fp.read()
    return text


def part_one(text):
    result = 0

    exp = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    for x, y in exp.findall(text):
        result += int(x) * int(y)

    return result


def part_two(text):
    result = 0
    do_flag = True

    exp = re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)")

    for m in exp.finditer(text):
        if m.group(0) == "don't()":
            do_flag = False
        elif m.group(0) == "do()":
            do_flag = True
        elif do_flag:
            x, y = m.groups()
            result += int(x) * int(y)

    return result


def main():
    text = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(text)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(text)}")


if __name__ == "__main__":
    main()
