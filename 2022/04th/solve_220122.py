# BOJ 1157
str = input().upper()
ar = [0 for _ in range(26)]
for s in str:
    ar[ord(s) - ord('A')] += 1
max_index = 0
max_count = 0
for i in range(26):
    if ar[max_index] < ar[i]:
        max_index = i
        max_count = ar[i]
if ar.count(ar[max_index]) > 1:
    print('?')
else:
    print(chr(ord('A') + max_index))
