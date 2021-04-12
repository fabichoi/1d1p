#boj 1495

if __name__ == "__main__":
    mn = 101
    mm = 1001

    n, s, m = map(int, input().split(' '))
    v = [0] + list(map(int, input().split(' ')))
    dp = [[False for __ in range(mm)] for _ in range(mn)]

    dp[0][s] = True
    Found = False

    for i in range(1, n+1):
        for j in range(mm):
            if dp[i-1][j]:
                up = j + v[i]
                down = j - v[i]
                if (up <= m):
                    dp[i][up] = True
                if (down >= 0):
                    dp[i][down] = True

    result = -1
    for i in range(mm):
        if dp[n][i]:
            result = i

    print(result)
