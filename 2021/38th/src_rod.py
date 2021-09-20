import sys

sys.setrecursionlimit(10 ** 5)


def solve(v, n):
    if n <= 0:
        return 0

    price = -987654321

    for i in range(1, n + 1):
        price = max(price, v[i] + solve(v, n - i))

    return price


cache = [0 for _ in range(100000)]


def solve_memo(v, n):
    if n <= 0:
        return 0
    global cache

    if cache[n - 1] != 0:
        return cache[n - 1]

    cache[n - 1] = -987654321

    for i in range(1, n + 1):
        cache[n - 1] = max(cache[n - 1], v[i] + solve_memo(v, n - i))

    return cache[n - 1]


if __name__ == '__main__':
    v = [0] + list(map(int, input().split()))
    # print(solve(v, len(v) - 1))
    print(solve_memo(v, len(v) - 1))
