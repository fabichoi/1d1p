# boj 1904
# 01타일

def solve(n):
    if n <= 3:
        return n
    a = 2
    b = 3
    for i in range(4, n+1):
        c = (a+b) % 15746
        a = b
        b = c
    return c

print(solve(int(input())))