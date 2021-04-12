# python file for week of 9 in 2021

import sys
for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split(' '))
    print('YES') if bin(a & (b-a)) == bin(b-a) else print('NO')


'''
import sys

n, q = map(int, sys.stdin.readline().split(' '))
ar = [-1] + list(map(int, sys.stdin.readline().split(' ')))

n1 = ar.count(1)
n0 = ar.count(0)

for _ in range(q):
    t, k = map(int, sys.stdin.readline().split(' '))
    if t == 1:
        if ar[k] == 1:
            ar[k] = 0
            n0 += 1
            n1 -= 1
        else:
            ar[k] = 1
            n0 -= 1
            n1 += 1
    else:
        if k > n1:
            print(0)
        else:
            print(1)

'''

'''
def get_over_num(n, m):
    a = int(n % m)
    if a == 0:
        return 0
    return m - int(n % m)

for _ in range(int(input())):
    p, a, b, c = map(int, input().split(' '))
    print(min(get_over_num(p, a), get_over_num(p, b), get_over_num(p, c)))
'''

'''
n, m = map(int, input().split(' '))
a, b = input(), input()

m_cnt = 0
idx = 0

for i in range(m):
    cnt = 0
    for j in range(idx, n):
        if b[i] == a[j]:
            cnt += 1
        else:
            idx = j
            break
    m_cnt = max(m_cnt, cnt)

print(m_cnt)
'''
