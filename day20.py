DAY = 20
PARTS = [1, 2]

import enum

INF = float("inf")

class Direction(enum.Enum):
    W = (0, -1)
    E = (0, +1)
    N = (-1, 0)
    S = (1, 0)

def taxicab_distance(point, other):
    return abs(point[0]-other[0]) + abs(point[1]-other[1])

class Graph:

    def __init__(self, vertices, max_x, max_y):
        self.vertices = vertices
        self.max_x = max_x
        self.max_y = max_y
        self.edges = self.get_edges()

    def get_neighbors(self, node):        
        x, y = node
        for d in Direction:
            #input(f"Walking {d} from {x,y}")
            dx, dy = d.value
            nx, ny = x + dx, y + dy
            if nx in range(self.max_x) and ny in range(self.max_y):
                if (nx, ny) in self.vertices:
                    yield (nx, ny)

    def get_taxicab_neighbors(self, node, distance, strict=True):
        x, y = node
        for dx in range(-distance, distance+1):
            if strict:
                dy_range = [-(distance - abs(dx)), (distance - abs(dx))] if distance != abs(dx) else [0]
            else:
                dy_range = range(abs(dx)-distance, distance-abs(dx)+1)
            for dy in dy_range:
                nx, ny = x+dx, y+dy
                if nx in range(self.max_x) and ny in range(self.max_y):
                    if (nx, ny) in self.vertices:
                        yield (nx, ny)


    def get_edges(self):
        edges = dict()
        for (r,c) in self.vertices:
            for step in self.get_neighbors((r,c)):
                if (r, c) not in edges:
                    edges[(r, c)] = []
                edges[(r, c)].append((step, 1))
        return edges

    def count_shortcuts(self, costs, shortcut_size, saving, strict=True):
        ret = 0
        for node in costs:
            for taxicab_neighbor in self.get_taxicab_neighbors(node, shortcut_size, strict=strict):
                if taxicab_neighbor in costs:
                    avoided_cost = costs[node] - costs[taxicab_neighbor]
                    shortcut_cost = taxicab_distance(taxicab_neighbor, node)
                    if avoided_cost - shortcut_cost >= saving:
                        ret += 1
        return ret


    def dijkstra(self, start, target):
        min_cost = {node: INF for node in self.edges}
        min_cost[start] = 0
        prev_node = {}
        unvisited = set(self.edges.keys())

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
            for neighbor, weight in self.edges.get(current_node, []):
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

        return path[::-1], min_cost

def parse_input():
    start, end = None, None
    size_x, size_y = 0, 0
    vertices = set()
    with open(f"day{DAY}.txt", "r") as fp:
        row, col = 0, 0 
        for line in fp:
            for char in line.strip():

                if char != '#':
                    vertices.add((row, col))

                if char == 'S':
                    start = (row, col)
                elif char == 'E':
                    end = (row, col)

                col += 1
            size_x = max(size_x, col)
            size_y = max(size_y, col)
            col = 0
            row += 1
    return vertices, start, end, size_x, size_y

def part_one(graph, start, end):
    path, costs = graph.dijkstra(start, end)
    result = graph.count_shortcuts(costs, 2, 100)

    return result

def part_two(graph, start, end):
    path, costs = graph.dijkstra(start, end)
    result = graph.count_shortcuts(costs, 20, 100, strict=False)

    return result


def main():
    vertices, start, end, size_x, size_y  = parse_input()
    g = Graph(vertices, size_x, size_y)
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(g, start, end)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(g, start, end)}")


if __name__ == "__main__":
    main()
