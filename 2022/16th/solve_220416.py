# BOJ 2097
import math
def solve(n):
    if n in [1, 2]:
        return 4
    a = int(math.sqrt(n))
    b = int(n / a)
    res = (a + b - 2) * 2
    if n != a * b:
        res += 2
    return res
print(solve(int(input())))
