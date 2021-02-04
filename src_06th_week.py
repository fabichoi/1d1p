'''
def solve(n):
    if int(n ** 0.5) ** 2 == n:
        return 1
    for i in range(1, int((n // 2) ** 0.5) + 1):
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if i ** 2 + j ** 2 == n:
                return 2
            elif (n - i ** 2 - j ** 2) ** 0.5 % 1 == 0:
                return 3
    return 4


print(solve(int(input())))
'''

'''
for _ in range(int(input())):
    cnt = 0
    n = int(input())
    while n > 1:
        if n % 2 != 0:
            cnt += 1
        n /= 2
    print("YES" if cnt > 1 else "NO")
'''
n = [2020 * i for i in range(501)]
m = [2021 * i for i in range(501)]
ar = []
for i in range(501):
    for j in range(501):
        ar.append(n[i] + m[j])

import sys
res = ""
for _ in range(int(sys.stdin.readline().rstrip())):
    if int(sys.stdin.readline().rstrip()) in ar:
        res += "YES\n"
    else:
        res += "NO\n"
print(res)