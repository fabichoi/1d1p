# boj 12865
# 평범한 배낭

def solve(n,k,w,v):
    dp = [[0 for _ in range(k+1)] for __ in range(n+1)]
    ret = 0

    for i in range(n):
        for j in range(k+1):
            if j + w[i] <= k:
                dp[i + 1][j + w[i]] = max(dp[i + 1][j + w[i]], dp[i][j] + v[i])
                ret = max(dp[i + 1][j + w[i]], ret)

    return ret

n,k = map(lambda x:int(x), input().split(' '))
w = []
s = []
for i in range(n):
    a, b = map(lambda x:int(x), input().split(' '))
    w.append(a)
    s.append(b)
print(solve(n,k,w,s))

'''
# boj 1904
# 01타일

def solve(n):
    if n <= 3:
        return n
    a = 2
    b = 3
    for i in range(4, n+1):
        c = (a+b) % 15746
        a = b
        b = c
    return c

print(solve(int(input())))

'''
