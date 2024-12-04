DAY = 2
PARTS = [1, 2]


def parse_input():
    with open(f"day{DAY}.txt", "r") as fp:
        lines = fp.readlines()
    return lines


def diff(vec):
    return [vec[i] - vec[i - 1] for i in range(1, len(vec))]


def part_one():
    result = 0
    lines = parse_input()

    for line_idx, line in enumerate(lines):
        report = line.split()
        increasing = True
        safe = True
        print(f"\nReport: {report}")

        for level_idx in range(1, len(report)):
            this = report[level_idx]
            prev = report[level_idx - 1]
            delta = int(this) - int(prev)

            if level_idx == 1:
                increasing = delta > 0
            elif (delta < 0 and increasing) or (delta > 0 and not (increasing)):
                safe = False
                break

            if abs(delta) < 1 or abs(delta) > 3:
                safe = False
                break

        if safe:
            print("Report safe")
            result += 1
        else:
            print("Report not safe")

        print(f"Safe reports {result}/{line_idx+1}")

    return result


def find_unsafe(report):
    unsafe_idx = None
    diff_report = diff(report)

    for idx, item in enumerate(diff_report):
        if (diff_report[0] * item <= 0) or (abs(item) > 3 or abs(item) < 1):
            unsafe_idx = idx + 1
            break

    return unsafe_idx

def is_safe(report):
    unsafe_idx = find_unsafe(report)
    if unsafe_idx:
        amended_report = report[:unsafe_idx] + report[unsafe_idx + 1 :]
        another_unsafe_idx = find_unsafe(amended_report)
        if another_unsafe_idx:
            return False
    return True

def part_two():
    result = 0
    reports = [[int(x) for x in y.split()] for y in parse_input()]

    for report in reports:
        if is_safe(report) or is_safe(report[::-1]):
            result += 1

    return result


def main():
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one()}")
        elif part == 2:
            print(f"Result for part {part} is {part_two()}")


if __name__ == "__main__":
    main()
