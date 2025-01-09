import sys

sys.setrecursionlimit(10 ** 5)


def solve_recur(m, n):
    if m == 0 and n == 0:
        return 0
    if m == 0 or n == 0:
        return 1

    return solve_recur(m - 1, n) + solve_recur(m, n - 1)


def solve_dp(y, x):
    cache = [[0 for _ in range(x)] for __ in range(y)]
    for i in range(1, x):
        cache[0][i] = 1
    for i in range(1, y):
        cache[i][0] = 1

    for i in range(1, y):
        for j in range(1, x):
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]

    return cache[y - 1][x - 1]


if __name__ == '__main__':
    y, x = map(int, input().split())
    print(solve_dp(y, x))
