
# boj 12865
# 평범한 배낭

def solve():
    ws = [3,4,1,2,3]
    ps = [2,3,2,3,6]

    maxw = 10

    def knapsack(n, w):
        if w > maxw:
            return -1
        if n >= len(ws):
            return 0
        return max(knapsack(n+1, w), knapsack(n+1, w+ws[n]) + ps[n])

    knapsack(0, 0)

print(solve())


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

