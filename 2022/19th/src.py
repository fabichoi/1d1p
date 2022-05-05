# Codeforces Round #787 (Div.3)
# G
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ar = list(map(int, input().split()))

res = 0
if n == 1:
    print(0)
elif n == 2:
    if ar[0] >= ar[1]:
        print(0)
    else:
        for _ in range(ar[1]):
            if ar[0] >= ar[1]:
                break
            ar[0] += 1
            ar[1] -= 1
            res += 1
        print(res)
else:
    for i in range(0, len(ar)-1):
        for _ in range(250):
            if ar[i] >= ar[i+1]:
                break
            ar[i] += 1
            ar[i+1] -= 1
            res += 1
    print(res)



'''
# B
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))

    res = 0
    if n == 1:
        print(0)
        continue
    if n == 2:
        if ar[1] == 0:
            print(-1)
            continue
        for _ in range(31):
            if ar[0] < ar[1]:
                break
            ar[0] = int(ar[0] / 2)
            res += 1
        print(res)
        continue

    impossible = False
    for i in range(len(ar) - 1, 0, -1):
        for _ in range(31):
            if ar[i - 1] < ar[i]:
                break
            ar[i - 1] = int(ar[i - 1] / 2)
            res += 1

    for i in range(len(ar) - 1):
        if ar[i + 1] <= ar[i]:
            impossible = True
            break

    if impossible:
        print(-1)
        continue
    print(res)
'''

'''
# A
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b, c, x, y = map(int, input().split())
    a -= x
    b -= y
    if c + a >= 0 and c + b >= 0 and c + a + b >= 0:
        print('YES')
        continue
    print('NO')
'''

'''
# BOJ 1951
ar = [(0, 0, 0)]
for i in range(10):
    a = 10 ** i
    b = (10 ** (i + 1)) - 1
    ar.append((a, b, ar[i][2] + (b - a + 1) * (i + 1)))
mod = 1234567
ar[0] = (0, 0, 0)

n = input()
res = 0
for i in range(10, 0, -1):
    if ar[i][0] <= int(n) <= ar[i][1]:
        z = int(n) - ar[i][0] + 1
        res = (res + z * i) % mod
        res = (res + ar[i-1][2]) % mod
        break
print(res)
'''

'''
# BOJ 2417
import math
i = int(input())
found = math.ceil(math.sqrt(i))
for f in range(found-5, found+5, 1):
    if f < 0:
        continue
    if i <= f * f:
        print(f)
        break
'''

'''
# BOJ 10825
import sys
input = sys.stdin.readline
class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def __repr__(self):
        return repr((self.name, self.kor, self.eng, self.math))
s = []
for _ in range(int(input())):
    name, kor, eng, math = input().split()
    s.append(Student(name,-int(kor),int(eng),-int(math)))
s = sorted(s, key=lambda s: (s.kor, s.eng, s.math, s.name))
res = ""
for i in range(len(s)):
    res += (s[i].name+"\n")
print(res)
'''

'''
# BOJ 1753
import heapq
import sys

s_input = sys.stdin.readline
v, e = map(int, s_input().split())
k = int(s_input())
edge = [[] for _ in range(v + 1)]
heap = []

for _ in range(e):
    a, b, c = map(int, s_input().split())
    edge[a].append((c, b))

dp = [float('inf') for _ in range(v + 1)]

dp[k] = 0
heapq.heappush(heap, (0, k))

while heap:
    weight, move = heapq.heappop(heap)

    if dp[move] < weight:
        continue

    for w, node in edge[move]:
        if w + weight < dp[node]:
            dp[node] = w + weight
            heapq.heappush(heap, (dp[node], node))

for i in range(1, v + 1):
    print("INF" if dp[i] == float('inf') else dp[i])
'''
