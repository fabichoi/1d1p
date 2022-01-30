# BOJ 1173
N, m, M, T, R = map(int, input().split())
res = 0
c = m
for _ in range(40000):
    if N == 0:
        break
    if c + T <= M:
        c += T
        N -= 1
    else:
        if c - R < m:
            c = m
        else:
            c -= R
    res += 1

print(-1 if res == 40000 else res)
