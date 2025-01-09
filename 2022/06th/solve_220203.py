# BOJ 1267
from sys import stdin

n = int(stdin.readline())
ar = map(int, stdin.readline().split(' '))
m, y = 0, 0
for i in ar:
    y += (i // 30) + 1
    m += (i // 60) + 1
y *= 10
m *= 15
if m > y:
    print('Y ' + str(y))
elif m < y:
    print('M ' + str(m))
else:
    print('Y M ' + str(m))
