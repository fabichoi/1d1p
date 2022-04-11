# BOJ 2033
n = input()
res = ""
last = 0
for i in range(len(n) - 1, 0, -1):
    nn = int(n[i]) + last
    if nn >= 5:
        last = 1
    else:
        last = 0
    res = str(0) + res
res = str(int(n[0]) + last) + res
print(res)
