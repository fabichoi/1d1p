# BOJ 1919


'''
# BOJ 1924
ar = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
for i in range(2, 13):
    ar[i] += ar[i-1]
r = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
m, d = map(int, input().split(' '))
print(r[(ar[m] + d) % 7])
'''

'''
# BOJ 1975
import sys

input = sys.stdin.readline
res = [0 for _ in range(1001)]
for i in range(2, 1001):
    for j in range(2, i+1):
        k = i
        while k > 0:
            if k % j == 0:
                k //= j
                res[i] += 1
            else:
                break

for _ in range(int(input())):
    print(res[int(input())])
'''

# print('YONSEI') if input() == '0' else print('Leading the Way to the Future')

'''
# BOJ 1996
import sys

input = sys.stdin.readline
pos_x = [0, 1, 1, 1, 0, -1, -1, -1]
pos_y = [-1, -1, 0, 1, 1, 1, 0, -1]

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))
res = [[0 for _ in range(n)] for __ in range(n)]


def fill_mines(board, x, y):
    if board[y][x] == '.':
        return
    v = int(board[y][x])

    for i in range(8):
        if x + pos_x[i] < 0 or y + pos_y[i] < 0 or x + pos_x[i] >= n or y + pos_y[i] >= n:
            continue
        res[y + pos_y[i]][x + pos_x[i]] += v


for y in range(n):
    for x in range(n):
        fill_mines(board, x, y)

for y in range(n):
    for x in range(n):
        if board[y][x] != '.':
            res[y][x] = '*'
        else:
            if int(res[y][x]) > 9:
                res[y][x] = 'M'

        print(res[y][x], end='')
    print('')
'''

'''
# BOJ 2010
import sys
input = sys.stdin.readline
res = -1
for _ in range(int(input())):
    n = int(input())
    if res == -1:
        res = n
        continue
    res += n - 1

print(res)
'''

'''
# BOJ 2037
ar = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']


def get_rept(ch):
    for i in range(2, 10):
        if ch in ar[i]:
            return (i, ar[i].find(ch) + 1)


p, w = map(int, input().split(' '))
s = input()
if len(s) < 2:
    print(p * get_rept(s[0]))
else:
    res = p * get_rept(s[0])[1]
    l = len(s)
    for i in range(1, l):
        if s[i] == ' ':
            res += p
            continue
        prev = get_rept(s[i - 1])
        curr = get_rept(s[i])
        res += p * curr[1]
        if not prev:
            continue
        if prev[0] == curr[0]:
            res += w
    print(res)
'''

'''
# BOJ 2028
for _ in range(int(input())):
    n = input()
    l = len(n)
    r = str(int(n) * int(n))
    if r[len(r)-l:] == n:
        print('YES')
        continue
    print('NO')
'''

'''
# BOJ 1408
start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))
r = end[0] * 3600 + end[1] * 60 + end[2] - (start[0] * 3600 + start[1] * 60 + start[2])
res = [str(r // 3600), str(r % 3600 // 60), str(r % 60)]
if int(res[0]) < 0:
    res[0] = str(int(res[0]) + 24)
if int(res[1]) < 0:
    res[1] = str(int(res[1]) + 60)
for i in range(3):
    if int(res[i]) < 10:
        res[i] = '0' + res[i]
print(':'.join(res))
'''
'''
# BOJ 1271
a, b = map(int, input().split())
print(a // b)
print(a % b)
'''

'''
# BOJ 1252
a, b = input().split()
a = int('0b' + a, 2)
b = int('0b' + b, 2)
print(bin(a + b)[2:])
'''
'''
# BOJ 2083
import sys

input = sys.stdin.readline
while True:
    name, age, weight = input().rstrip().split(' ')
    if [name, age, weight] == ['#', '0', '0']:
        break
    if int(age) > 17 or int(weight) >= 80:
        print(name + ' Senior')
        continue
    print(name + ' Junior')
'''

'''
# BOJ 2139
import sys

input = sys.stdin.readline
cal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    cal[2] = 28
    d, m, y = map(int, input().split(' '))
    if [d, m, y] == [0, 0, 0]:
        break
    if not y % 4:
        cal[2] = 29
        if not y % 100:
            cal[2] = 28
    if not y % 400:
        cal[2] = 29
    print(d + sum(cal[:m]))
'''

'''
# BOJ 4419
n = int(input())
bs, c = [], ['']
for _ in range(n):
    c.append(input().rstrip())

nb = 0
for _ in range(1000):
    try:
        bs.append(list(map(int, input().split())))
        nb += 1
    except EOFError:
        break

eliminated = [False for _ in range(n + 1)]
while True:
    vote = [0 for _ in range(n + 1)]

    for b in bs:
        while True:
            if not eliminated[b[0]]:
                break
            b.pop(0)
        vote[b[0]] += 1

    max_v = max(vote[1:])

    if max_v >= nb / 2:
        for i in range(1, n + 1):
            if vote[i] == max_v:
                print(c[i])
        break

    min_v = 1000
    for i in range(1, n + 1):
        if eliminated[i]:
            continue
        if min_v > vote[i]:
            min_v = vote[i]

    if max_v == min_v:
        for i in range(1, n + 1):
            if vote[i] == max_v:
                print(c[i])
        break

    for i in range(1, n + 1):
        if vote[i] == min_v:
            eliminated[i] = True
'''
