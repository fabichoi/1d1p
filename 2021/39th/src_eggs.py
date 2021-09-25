import sys

sys.setrecursionlimit(10 ** 5)


def solve(n, x):
    if n == 1 or n == 0 or x == 1:
        return n

    init = 987654321

    for p in range(1, n + 1):
        broken = solve(p - 1, x - 1)
        okay = solve(n - p, x)
        now = max(broken, okay)
        init = min(init, now)

    return init + 1


if __name__ == '__main__':
    n, x = map(int, input().split())
    print(solve(n, x))
