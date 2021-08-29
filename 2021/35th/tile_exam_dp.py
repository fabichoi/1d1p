import sys

sys.setrecursionlimit(10 ** 5)

dp = [0, 1, 2] + [-1 for _ in range(1000)]

if __name__ == '__main__':
    n = int(input())

    for i in range(3, 1001):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    print(dp[n])
