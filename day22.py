DAY = 22
PARTS = [1, 2]

secrets_memo = dict()
mix_memo = dict()
prune_memo = dict()


def next_secret(n):
    if n not in secrets_memo:
        next_secret = prune(mix(n, n * 64))
        next_secret = prune(mix(next_secret // 32, next_secret))
        next_secret = prune(mix(next_secret * 2048, next_secret))
        secrets_memo[n] = next_secret
    return secrets_memo[n]


def mix(value, secret):
    if (value, secret) not in mix_memo:
        mix_memo[(value, secret)] = value ^ secret
    return mix_memo[(value, secret)]


def prune(value):
    if value not in prune_memo:
        prune_memo[value] = value % 16777216
    return prune_memo[value]


def lsd(value):
    return value % 10


def parse_input():
    buyers = list()
    with open(f"day{DAY}.txt", "r") as fp:
        for line in fp:
            buyers.append(int(line.strip()))
    return buyers


def diff(series):
    return [series[idx] - series[idx - 1] for idx in range(1, len(series))]


def part_one(buyers):
    result = 0
    for b in buyers:
        for _ in range(2000):
            b = next_secret(b)
        result += b
    return result


def part_two(buyers):
    sequences = dict()

    for b in buyers:
        secret = b
        cur_sequence = list()
        seen = set()
        for idx in range(2000):
            prev_secret = secret
            secret = next_secret(prev_secret)
            price = lsd(secret)
            delta = price - lsd(prev_secret)
            cur_sequence = (
                cur_sequence
                + [
                    delta,
                ]
            )[-4:]
            if len(cur_sequence) == 4:
                cur_sequence_t = tuple(cur_sequence)
                if cur_sequence_t in seen:
                    continue
                if cur_sequence_t not in sequences:
                    sequences[cur_sequence_t] = 0
                sequences[cur_sequence_t] += price
                seen.add(cur_sequence_t)

    return max(sequences.values())


def main():

    # assert mix(15, 42) == 37
    # assert prune(100000000) == 16113920

    # secret = 123
    # for x in (
    #     15887950,
    #     16495136,
    #     527345,
    #     704524,
    #     1553684,
    #     12683156,
    #     11100544,
    #     12249484,
    #     7753432,
    #     5908254,
    # ):
    #     secret = next_secret(secret)
    #     print(f"New secret: {secret}")
    #     assert secret == x

    buyers = parse_input()
    for part in PARTS:
        if part == 1:
            print(f"Result for part {part} is {part_one(buyers)}")
        elif part == 2:
            print(f"Result for part {part} is {part_two(buyers)}")


if __name__ == "__main__":
    main()
