import sys
sys.setrecursionlimit(10**5)

def solve(c, weight, value, n):
    if n <= 0 or c <= 0:
        return 0

    if weight[n-1] > c:
        return solve(c, weight, value, n-1)

    carry = value[n-1] + solve(c - weight[n-1], weight, value, n-1)
    leave = solve(c, weight, value, n-1)

    return max(carry, leave)

if __name__ == '__main__':
    n, c = map(int, input().split())
    weight = []
    value = []
    for _ in range(n):
        a, b = map(int, input().split())
        weight.append(a)
        value.append(b)

    print(solve(c, weight, value, n))

