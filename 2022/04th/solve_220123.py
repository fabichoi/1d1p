# BOJ 1159
d = dict()
for _ in range(int(input())):
    i = input()[0]
    if d.get(i) is None:
        d[i] = 1
        continue
    d[i] += 1
sorted_d = sorted(d.items())
res = ''
for r in sorted_d:
    if r[1] >= 5:
        res += r[0]
print(res if len(res) > 0 else 'PREDAJA')
