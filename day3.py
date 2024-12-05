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

    for (x,y) in exp.findall(text):
        result += int(x) * int(y)

    return result

def part_two(text):
    result = 0
    do_flag = True

    do_exp = re.compile(r"do\(\)")
    dont_exp = re.compile(r"don't\(\)")
    exp = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    dos = [do.span()[1] for do in do_exp.finditer(text)]
    donts = [dont.span()[1] for dont in dont_exp.finditer(text)]

    print(dos)
    print(donts)

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
