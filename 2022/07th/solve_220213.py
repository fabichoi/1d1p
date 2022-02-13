# BOJ 1356
n = list(map(int, input()))
l = len(n)
answer = "NO"
if l < 3:
    if l == 2 and n[0] == n[1]:
        answer = "YES"
else:
    for i in range(1, l):
        a, b = 1, 1
        for j in range(l - i):
            a *= n[j]
        for k in range(j + 1, l):
            b *= n[k]
        if a == b:
            answer = "YES"
print(answer)
