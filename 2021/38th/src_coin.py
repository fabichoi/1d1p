import sys
sys.setrecursionlimit(10**5)
def minCoins(coin, n, s):
    if s == 0:
        return 0
    result = 987654321
    for i in range(n):
        if coin[i] <= s:
            temp = minCoins(coin, n, s - coin[i])

            if temp + 1 < result:
                result = temp + 1
    return result

MAX_INT = 9876543210

def minCoins_dp(coin, n, s):
    ar = [MAX_INT for _ in range(s+1)]
    ar[0] = 0

    for i in range(1, s+1):
        for j in range(n):
            if coin[j] <= i:
                temp = ar[i - coin[j]]
                if temp != MAX_INT and temp + 1 < ar[i]:
                    ar[i] = temp + 1

    return ar[s]

coin = list(map(int, input().split()))
s = int(input())
n = len(coin)
print(minCoins_dp(coin, n, s))
