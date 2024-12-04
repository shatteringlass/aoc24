DAY = 1


def main():
    result = 0

    with open(f'day{DAY}.txt', 'r') as fp:
        lines = fp.readlines()

    left, right = [sorted([row.split()[col] for row in lines]) for col in (0,-1)]
    
    for pair_idx in range(len(lines)):
        result += abs(int(left[pair_idx]) - int(right[pair_idx]))
    
    print(f"The result is {result}.")


if __name__ == '__main__':
    main()
