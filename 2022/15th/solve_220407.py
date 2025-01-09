# BOJ 1977
from math import sqrt

n = int(input())
m = int(input())

nn = int(sqrt(n))
mm = int(sqrt(m))

a, b = -1, 0
for i in range(nn, mm+1):
    k = i ** 2
    if k < n or k > m:
        continue
    if a == -1:
        a = k
    b += k

if a != -1:
    print(b)
print(a)
