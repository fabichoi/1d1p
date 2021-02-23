# python file for week of 9 in 2021

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
