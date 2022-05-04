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
