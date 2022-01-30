# BOJ 1236
from sys import stdin

n, m = map(int, stdin.readline().split(' '))
m_count = 0
init_n = ['.' for _ in range(m)]
for i in range(n):
    l = stdin.readline()
    for j in range(m):
        if l[j] == 'X':
            init_n[j] = 'X'
    if l.count('X') < 1:
        m_count += 1

print(max(init_n.count('.'), m_count))
