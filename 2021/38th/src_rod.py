import sys

sys.setrecursionlimit(10 ** 5)


def solve(v, n):
    if n <= 0:
        return 0

    price = -987654321

    for i in range(1, n + 1):
        price = max(price, v[i] + solve(v, n - i))

    return price


if __name__ == '__main__':
    v = [0] + list(map(int, input().split()))
    print(solve(v, len(v) - 1))
