DAY = 13
PARTS = [1, 2]


class ClawProblem:

    def __init__(self, increments, costs, prize):
        self.increments = increments
        self.prize = prize
        self.costs = costs

    def solve(self):
        # Return the solution to the linear equation system, if it is a non-negative integer
        prize_x, prize_y = self.prize
        ((a_x, a_y), (b_x, b_y)) = self.increments
        x = (prize_x * b_y - prize_y*a_y) / (a_x*b_y - a_y*b_x)
        y = (prize_x - a_x*x)/a_y
        if x >= 0 and y >= 0 and int(x) == x and int(y) == y:
            return (int(x), int(y))
        return None

    def cost(self):
        try:
            sol_x, sol_y = self.solve()
            return sol_x * self.costs[0] + sol_y * self.costs[1]
        except Exception:
            return None

    def __repr__(self):
        return f"{self.__class__.__name__}(increments={self.increments}, prize={self.prize}, costs={self.costs})"


def parse_input():
    problems = list()
    with open(f"day{DAY}.txt", "r") as fp:
        for block in fp.read().split('\n\n'):
            a, b, coords = block.split('\n')
            a_x, a_y = tuple(int(c.split('+')[1]) for c in a.split(','))
            b_x, b_y = tuple(int(c.split('+')[1]) for c in b.split(','))
            problem = ClawProblem(
                increments=(
                    (a_x, b_x),
                    (a_y, b_y)
                ),
                costs=(3, 1),
                prize=tuple(int(c.split('=')[1]) for c in coords.split(','))
            )
            problems.append(problem)
    return problems


def part_one(problems):
    result = 0

    for problem in problems:
        cost = problem.cost()
        if cost:
            result += cost

    return result


def part_two(problems):
    result = 0
    offset = 10e12
    for problem in problems:
        px, py = problem.prize
        problem.prize = (px + offset, py+offset)
        cost = problem.cost()
        if cost:
            result += cost
    return result


def main():
    problems = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(problems)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(problems)}")


if __name__ == "__main__":
    main()
