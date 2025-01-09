import sys

sys.setrecursionlimit(10 ** 5)


def solve(s, start, end):
    if start > end:
        return 0
    if start == end:
        return 1

    if s[start] == s[end]:
        return solve(s, start + 1, end - 1) + 2
    else:
        left = solve(s, start, end - 1)
        right = solve(s, start + 1, end)
        return left if left > right else right


def solve_dp(s):
    n = len(s)

    if n == 0:
        return 0

    cache = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        cache[i][i] = 1

    for k in range(2, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and k == 2:
                cache[i][j] = 2
            elif s[i] == s[j]:
                cache[i][j] = cache[i + 1][j - 1] + 2
            else:
                cache[i][j] = cache[i][j - 1] if cache[i][j - 1] > cache[i + 1][j] else cache[i + 1][j]

    return cache[0][n - 1]


if __name__ == '__main__':
    s = input()
    # print(solve(s, 0, len(s) - 1))
    print(solve_dp(s))
