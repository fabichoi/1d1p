# boj 2170
'''
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())
    res = 0
    ar = []
    for _ in range(n):
        ar.append(list(map(int, stdin.readline().split(' '))))
    ar.sort(key=lambda x : (x[0], x[1]))

    ma, mb = ar[0][0], ar[0][1]
    for i in range(1, n):
        a, b = ar[i][0], ar[i][1]
        if ma <= a and mb >= b:
            continue

        if mb < a:
            res += mb - ma
            ma = a
            mb = b
        else:
            ma = min(ma, a)
            mb = max(mb, b)

    res += mb - ma
    print(res)
'''

# BOJ 7571

from sys import stdin

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split(' '))
    x = [0 for _ in range(m)]
    y = [0 for _ in range(m)]
    mx, my = 0, 0
    res = 0
    for i in range(m):
        x[i], y[i] = map(int, stdin.readline().split(' '))
    x.sort()
    y.sort()

    mx = x[m // 2]
    my = y[m // 2]
    for i in range(m):
        res += abs(x[i]-mx) + abs(y[i]-my)

    print(res)


