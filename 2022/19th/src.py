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
