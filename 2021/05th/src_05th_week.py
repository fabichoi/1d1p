'''
r, b = map(int, input().split(' '))
w = 0
for l in range(1, b+1):
    if b % l != 0:
        continue
    w = b // l
    sum = w * 2 + l * 2 + 4
    if sum == r:
        if w > l:
            print(str(w + 2) + " " + str(l + 2))
        else:
            print(str(l + 2) + " " + str(w + 2))
        break
'''

'''
t, w = map(int, input().split(' '))
p = [0]
for _ in range(t):
    p.append(int(input()) - 1)
'''

import sys

sys.setrecursionlimit(10 ** 9)

if __name__ == "__main__":
    t, w = map(int, input().split(' '))
    p = [0 for _ in range(t + 1)]
    for i in range(1, t + 1):
        p[i] = int(input())

    dp = [[[0, 0] for _ in range(w + 1)] for __ in range(t + 1)]

    for i in range(1, t + 1):
        dp[i][0][0] = dp[i - 1][0][0]
        dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0])
        if p[i] == 1:
            dp[i][0][0] += 1
        else:
            dp[i][1][1] += 1

    for i in range(2, t + 1):
        for j in range(1, w + 1):
            dp[i][j][0] = max(dp[i - 1][j - 1][1], dp[i - 1][j][0])
            dp[i][j][1] = max(dp[i - 1][j - 1][0], dp[i - 1][j][1])
            if p[i] == 1:
                dp[i][j][0] += 1
            else:
                dp[i][j][1] += 1

    result = 0
    for j in range(w+1):
        for k in range(2):
            if dp[t][j][k] > result:
                result = dp[t][j][k]
    print(result)

