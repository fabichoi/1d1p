# BOJ 1233
from sys import stdin

n, m, l = map(int, stdin.readline().split(' '))
d = dict()
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(1, l + 1):
            s = i + j + k
            d.setdefault(s, 0)
            d[s] += 1
print(sorted(d.items(), key=lambda x: (x[1], -x[0]), reverse=True)[0][0])
