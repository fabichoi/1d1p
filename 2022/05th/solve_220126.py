# BOJ 1212
aa = input()
ar = ['000', '001', '010', '011', '100', '101', '110', '111']
res = ''
for a in aa:
    res += ar[int(a)]
print('0' if res == '000' else res.lstrip('0'))
