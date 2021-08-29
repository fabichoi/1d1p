import sys

sys.setrecursionlimit(10 ** 5)

dp = [0, 1, 2] + [-1 for _ in range(1000)]


def solve(n):
    if dp[n] != -1:
        return dp[n]

    dp[n] = solve(n - 1) + solve(n - 2)
    return dp[n]


if __name__ == '__main__':
    n = int(input())
    print(solve(n) % 10007)
