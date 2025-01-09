import sys

sys.setrecursionlimit(10 ** 5)


def solve(s1, s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    if s1[0] == s2[0]:
        return solve(s1[1:], s2[1:])

    d = solve(s1[1:], s2)
    u = solve(s1[1:], s2[1:])
    i = solve(s1, s2[1:])

    return min(d, u, i) + 1


def solve_dp(s1, s2):
    m, n = len(s1) + 1, len(s2) + 1
    ar = [[0 for _ in range(m)] for __ in range(n)]

    for i in range(n):
        ar[i][0] = i
    for i in range(m):
        ar[0][i] = i

    for i in range(1, m):
        for j in range(1, n):
            if s1[j - 1] == s2[i - 1]:
                ar[i][j] = ar[i - 1][j - 1]
            else:
                ar[i][j] = min(ar[i][j - 1], ar[i - 1][j], ar[i - 1][j - 1]) + 1

    return ar[n - 1][m - 1]


if __name__ == '__main__':
    # print(solve(input(), input()))
    print(solve_dp(input(), input()))
