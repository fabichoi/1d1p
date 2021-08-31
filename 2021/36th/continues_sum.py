def solve(n, ar):
    res = -100000000

    for i in range(n):
        temp = 0
        for j in range(i, n):
            temp += ar[j]
            if temp > res:
                res = temp

    return res


def solve_kadane(n, ar):
    res = -100000000
    temp = 0
    neg_max = -100000000
    neg_cnt = 0

    for i in range(n):
        temp += ar[i]

        if neg_max < ar[i]:
            neg_max = ar[i]

        if ar[i] < 0:
            neg_cnt += 1

        if temp < 0:
            temp = 0

        if res < temp:
            res = temp

    return neg_max if neg_cnt == n else res


def solve_dp(n, ar):
    dp = [0 for _ in range(n)]
    dp[0] = ar[0]

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + ar[i], ar[i])

    return max(dp)


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))
    # print(solve(n, ar))
    # print(solve_kadane(n, ar))
    print(solve_dp(n, ar))
