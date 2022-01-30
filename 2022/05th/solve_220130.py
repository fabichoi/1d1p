# BOJ 1247
from sys import stdin
for _ in range(3):
    s = 0
    for __ in range(int(stdin.readline())):
        s += int(stdin.readline())
    if s > 0:
        print('+')
    elif s < 0:
        print('-')
    else:
        print('0')