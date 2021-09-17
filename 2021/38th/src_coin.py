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

coin = list(map(int, input().split()))
s = int(input())
n = len(coin)
print(minCoins(coin, n, s))
