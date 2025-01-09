import sys

sys.setrecursionlimit(10 ** 5)


def solve(c, weight, value, n):
    if n <= 0 or c <= 0:
        return 0

    if weight[n - 1] > c:
        return solve(c, weight, value, n - 1)

    carry = value[n - 1] + solve(c - weight[n - 1], weight, value, n - 1)
    leave = solve(c, weight, value, n - 1)

    return max(carry, leave)


def solve_dp(c, weight, value, n):
    cache = [[0 for _ in range(c + 1)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if weight[i - 1] <= j:
                x = j - weight[i - 1]
                cache[i][j] = max(value[i - 1] + cache[i - 1][x], cache[i - 1][j])
            else:
                cache[i][j] = cache[i - 1][j]

    return cache[n][c]


if __name__ == '__main__':
    n, c = map(int, input().split())
    weight = []
    value = []
    for _ in range(n):
        a, b = map(int, input().split())
        weight.append(a)
        value.append(b)

    print(solve_dp(c, weight, value, n))
