import enum

DAY = 18
PARTS = [1, 2]

GRID_SIZE = 71
LIMIT = 1024
INF = float("inf")


class Direction(enum.Enum):
    W = (0, -1)
    E = (0, +1)
    N = (-1, 0)
    S = (1, 0)


def valid_steps(position, obstacles):
    x, y = position
    for d in Direction:
        #input(f"Walking {d} from {x,y}")
        dx, dy = d.value
        nx, ny = x + dx, y + dy
        if nx in range(GRID_SIZE) and ny in range(GRID_SIZE):
            if (nx, ny) not in obstacles:
                yield (nx, ny)
            else:
                print(f"Obstacle detected at {nx, ny}")
        else:
            print(f"Node {nx, ny} out of bounds")


def get_graph(obstacles):
    graph = dict()
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if (r, c) not in obstacles:
                for step in valid_steps((r, c), obstacles):
                    if (r, c) not in graph:
                        graph[(r, c)] = []
                    graph[(r, c)].append((step, 1))
    return graph


def dijkstra(graph, start, target):
    min_cost = {node: INF for node in graph}
    min_cost[start] = 0
    prev_node = {}
    unvisited = set(graph.keys())

    while unvisited:
        # cheapest unvisited node
        current_node = None
        current_cost = INF
        for node in unvisited:
            if min_cost.get(node, INF) < current_cost:
                current_cost = min_cost[node]
                current_node = node

        # no more nodes
        if current_node is None or current_cost == INF:
            break

        # mark as visited
        unvisited.remove(current_node)

        # update neighbors
        for neighbor, weight in graph.get(current_node, []):
            new_cost = min_cost[current_node] + weight
            if new_cost < min_cost.get(neighbor, INF):
                min_cost[neighbor] = new_cost
                prev_node[neighbor] = current_node

    path = []
    node = target
    while node in prev_node:
        path.append(node)
        node = prev_node[node]
    if path or start == target:
        path.append(start)

    return path[::-1], min_cost.get(target, INF)


def print_graph(graph):
    return [['.' if (r, c) in graph else '#' for c in range(GRID_SIZE)] for r in range(GRID_SIZE)]


def parse_input():
    falling_bytes = set()
    cnt = 0
    with open(f"day{DAY}.txt", "r") as fp:
        for line in fp:
            if cnt == LIMIT:
                break
            falling_bytes.add(tuple(map(int, (x for x in line.split(",")))))
            cnt += 1
    return falling_bytes


def part_one(falling_bytes):
    graph = get_graph(falling_bytes)
    for row in print_graph(graph):
        print(''.join(row))
    path, cost = dijkstra(graph, (0, 0), (GRID_SIZE-1, GRID_SIZE-1))
    return cost


def part_two(falling_bytes):
    result = 0

    return result


def main():
    falling_bytes = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(falling_bytes)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(falling_bytes)}")


if __name__ == "__main__":
    main()
