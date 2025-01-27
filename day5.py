DAY = 5
PARTS = [1, 2]


def parse_input():
    rules = []
    updates = []

    with open(f"day{DAY}.txt", "r") as fp:
        rules, updates = fp.read().split("\n\n")
        rules = [tuple(int(x) for x in r.split("|"))
                 for r in rules.split("\n")]
        updates = [tuple(int(x) for x in u.split(","))
                   for u in updates.split("\n")]

    return rules, updates


def parse_rules(rules):
    result = {}
    for before, after in rules:
        befores = result.setdefault(after, [])
        befores.append(before)
    return result


def check_order(before, after, rules):
    return not after in rules.get(before, [])


def part_one(rules, updates):
    result = 0

    for u in updates:

        ordered = True

        for idx in range(1, len(u)):
            if not check_order(u[idx - 1], u[idx], rules):
                ordered = False
                break

        if ordered:
            result += u[len(u) // 2]

    return result


def reorder(update, rules):
    if len(update) <= 1:
        return update

    ls, rs = [], []
    l = update[0]
    for r in update[1:]:
        if check_order(r, l, rules):
            # keep r before l
            ls.append(r)
        else:
            # move r after l
            rs.append(r)

    return reorder(ls, rules) + [l] + reorder(rs, rules)



def part_two(rules, updates):
    result = 0

    for u in updates:
        for idx in range(1, len(u)):
            if not check_order(u[idx - 1], u[idx], rules):
                reordered = reorder(u, rules)
                result += reordered[len(reordered) // 2]
                break

    return result


def main():
    rules, updates = parse_input()
    rules = parse_rules(rules)
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(rules, updates)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(rules, updates)}")


if __name__ == "__main__":
    main()
