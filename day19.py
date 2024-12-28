DAY = 19
PARTS = [1, 2]


def parse_input():
    with open(f"day{DAY}.txt", "r") as fp:
        patterns = set()
        words = set()
        i = 0
        for line in fp:
            if line == '\n':
                i += 1
            else:
                if i == 0:
                    patterns.update(line.strip().split(', '))
                else:
                    words.add(line.strip())

    return patterns, words


def check_design(words, patterns):
    if words in patterns:
        return True
    result = False
    for i in range(1, len(words)):
        if words[:i] in patterns:
            result |= check_design(words[i:], patterns)
        if result:
            break
    return result


def count_combinations(target, dictionary):
    memo = {}
    def dfs(start):
        if start == len(target):  # Reached the end of the string
            return 1
        if start in memo:  # Return cached result
            return memo[start]
        total = 0
        for s in dictionary:
            if target.startswith(s, start):  # Check if substring `s` matches at `start`
                total += dfs(start + len(s))  # Recursively explore remaining string
        memo[start] = total  # Cache result for current position
        return total
    return dfs(0)

def part_one(patterns, words):
    return sum((check_design(r, patterns) for r in words))


def part_two(patterns, words):
    result = 0
    for word in words:
        combos = count_combinations(word, patterns)
        result += combos
    return result


def main():
    patterns, words = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(patterns, words)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(patterns, words)}")


if __name__ == "__main__":
    main()
