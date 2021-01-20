'''
from sys import stdin

if __name__ == "__main__":
    n, l = map(int, stdin.readline().split(' '))
    p = [[int(x) for x in stdin.readline().split(' ')] for i in range(n)]

    p.sort()

    res, s = 0, 0

    for i in range(n):
        s = max(p[i][0], s)
        count = (p[i][1] - s + l - 1) // l
        res += count
        s += count * l

    print(res)
'''

'''
from sys import stdin

if __name__ == "__main__":
    for _ in range(int(stdin.readline())):
        n = int(stdin.readline().split()[0])
        b = stdin.readline().split()[0]
        a = ['1' for _ in range(n)]
        for i in range(1, n):
            t = int(b[i-1]) + int(a[i-1])
            if t == 2:
                if b[i] == '1':
                    a[i] = '0'
                else:
                    a[i] = '1'
            elif t == 1:
                if b[i] == '1':
                    a[i] = '1'
                else:
                    a[i] = '0'
            else:
                a[i] = '1'
        print(''.join(a))
'''

from sys import stdin

if __name__ == "__main__":
    m = 50000
    a = [True for _ in range(m)]
    che = []
    for i in range(2, m):
        if not a[i]:
            continue
        for j in range(2*i, m, i):
            a[j] = False
    for i in range(1, m):
        if a[i]:
            che.append(i)
    l = len(che)

    for _ in range(int(stdin.readline())):
        d = int(stdin.readline())
        res1, res2 = 0, 0
        i1 = 0
        for i in range(1, l):
            if che[i] - 1 >= d:
                res1 = che[i]
                i1 = i
                break
        for j in range(i1, l):
            if che[j] - res1 >= d:
                res2 = che[j]
                break

        print(res1 * res2)



