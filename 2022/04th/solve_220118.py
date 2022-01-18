# BOJ 1100
res = 0
for i in range(8):
    ar = input()
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 1:
                continue
            if ar[j] == 'F':
                res += 1
    else:
        for j in range(8):
            if j % 2 == 0:
                continue
            if ar[j] == 'F':
                res += 1
print(res)
