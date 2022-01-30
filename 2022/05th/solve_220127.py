# BOJ 1225
from sys import stdin

a, b = stdin.readline().split()
s = 0
aa = 0
for i in range(len(a)):
    aa += int(a[i])
for i in range(len(b)):
    s += aa * int(b[i])
print(s)
