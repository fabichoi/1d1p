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
