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


def solve_dp(n, x):
    cache = [[0 for _ in range(n + 1)] for __ in range(x + 1)]
    for i in range(1, x + 1):
        cache[i][1] = 1

    for j in range(1, n + 1):
        cache[1][j] = j

    for i in range(2, x + 1):
        for j in range(2, n + 1):
            cache[i][j] = 987654321

            for k in range(1, j + 1):
                now = 1 + max(cache[i - 1][k - 1], cache[i][j - k])
                if now < cache[i][j]:
                    cache[i][j] = now

    return cache[x][n]


if __name__ == '__main__':
    n, x = map(int, input().split())
    print(solve_dp(n, x))
