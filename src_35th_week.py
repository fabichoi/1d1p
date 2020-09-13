# Codeforces Round #670 (Div. 2)
# problem 1
'''
def solve():
    res = []
    for _ in range(int(input())):
        l = int(input())
        arr = list(map(lambda x:int(x), input().split(' ')))
        dl = [0 for _ in range(101)]

        for ar in arr:
            dl[ar] += 1

        r = 0
        cnt = 0
        i = 0
        while i < 101:
            if dl[i] == 0:
                r += i
                cnt += 1
                i -= 1
            elif dl[i] == 1:
                for j in range(i, 101):
                    dl[j] += 1
                r += i
                cnt += 1
            if cnt >= 2:
                break
            i += 1

        res.append(r)

    return res

for s in solve():
    print(s)
'''

# Codeforces Round #670 (Div. 2)
# problem 2
'''
def solve():
    res = []
    for _ in range(int(input())):
        n = int(input())
        l = list(map(lambda x: int(x), input().split(' ')))
        mul = 1
        if n == 5:
            for ll in l:
                mul = mul * ll
            res.append(mul)
        else:
            l.sort()
            res.append(max(
                l[0] * l[1] * l[2] * l[3] * l[4],
                l[-1] * l[-2] * l[-3] * l[-4] * l[-5],
                l[0] * l[1] * l[2] * l[3] * l[-1],
                l[-1] * l[-2] * l[-3] * l[-4] * l[0],
                l[0] * l[1] * l[2] * l[-2] * l[-1],
                l[-1] * l[-2] * l[-3] * l[0] * l[1],
                l[0] * l[1] * l[-3] * l[-2] * l[-1],
                l[-1] * l[-2] * l[0] * l[1] * l[2],
            ))
    return res

for s in solve():
    print(s)

'''


# boj 12865
# 평범한 배낭


def solve(n, k, w, v):
    dp = [[0 for _ in range(k + 1)] for __ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            if j - w[i] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i])

    return dp[n][k]


n, k = map(lambda x: int(x), input().split(' '))
w = [0]
v = [0]
for i in range(n):
    a, b = map(lambda x: int(x), input().split(' '))
    w.append(a)
    v.append(b)
print(solve(n, k, w, v))

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
