def solve(ar, n, x):
    if x == 0:
        return True
    if n == 0:
        return False
    if ar[0] > x:
        return solve(ar[1:], n - 1, x)

    return solve(ar[1:], n - 1, x) or solve(ar[1:], n - 1, x - ar[0])


def solve_dp(ar, n, x):
    subsum = [[False for _ in range(n)] for __ in range(x + 1)]

    for i in range(n):
        subsum[i][0] = True

    for j in range(1, x + 1):
        if ar[0] == j:
            subsum[0][j] = True
        else:
            subsum[0][j] = False

    for i in range(1, n):
        v = ar[i]
        for j in range(1, x + 1):
            if j < v:
                subsum[i][j] = subsum[i - 1][j]
            elif subsum[i - 1][j]:
                subsum[i][j] = True
            else:
                subsum[i][j] = subsum[i - 1][j - v]

    return subsum[n - 1][x]


if __name__ == '__main__':
    ar = list(map(int, input().split()))
    n = len(ar)
    x = int(input())
    # print(solve(ar, n, x))
    print(solve(ar, n, x))
