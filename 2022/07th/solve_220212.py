# BOJ 1350
n = int(input())
files = map(int, input().split(' '))
cluster = int(input())
res = 0
for file in files:
    if file == 0:
        continue
    m = file // cluster
    if file % cluster > 0:
        m += 1
    res += cluster * m
print(res)
