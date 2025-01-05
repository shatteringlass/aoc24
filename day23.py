DAY = 23
PARTS = [1, 2]

from itertools import combinations


def parse_input():
    links = {}
    with open(f"day{DAY}.txt", "r") as fp:
        for line in fp:
            a, b = line.strip().split("-")
            if a not in links:
                links[a] = []
            links[a].append(b)
            if b not in links:
                links[b] = []
            links[b].append(a)
    return links


def part_one(links):
    result = len(get_triples(links))

    return result


def part_two(links):
    max_clique = get_max_clique(links)

    return get_password(max_clique)


def grow_clique(clique, links):
    clique = set(clique)
    while True:
        for x in clique:
            for y in links.get(x):
                if set(links.get(y)).issuperset(clique):
                    # the neighbors of this node's neighbor contain the clique
                    clique.add(y)
                    break
            else:
                # x has no neighbors
                continue
            break
        else:
            # the clique is empty
            break
    return clique


def get_max_clique(links):
    triples = get_triples(links, only_t=False)
    max_clique = set()
    visited = set()

    for a, b, c in triples:
        if a in visited:
            continue
        clique = grow_clique((a, b, c), links)
        visited.update(clique)
        max_clique = max(max_clique, clique, key=len)

    return max_clique


# def is_clique(subset, links):
#     for u, v in combinations(subset, 2):
#         if u not in links.get(v, []) or v not in links.get(u, []):
#             return False
#     return True


# def get_max_clique(links):
#     nodes = set(list(links.keys()) + list(x for i in links.values() for x in i))

#     max_degree = max(len(v) for v in links.values())

#     for size in range(max_degree + 1, 1, -1):
#         for subset in combinations(nodes, size):
#             if is_clique(subset, links):
#                 return subset


def get_password(computers):
    return ",".join(sorted(computers))


def get_triples(links, only_t=True):
    triples = set()
    for src, dests in links.items():
        for dest in dests:
            for nxt in links[dest]:
                if src in links[nxt] or nxt in dests:
                    if not (only_t) or (
                        only_t
                        and (
                            src.startswith("t")
                            or dest.startswith("t")
                            or nxt.startswith("t")
                        )
                    ):
                        triples.add(frozenset([src, dest, nxt]))
    return triples


def main():
    links = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(links)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(links)}")


if __name__ == "__main__":
    main()
