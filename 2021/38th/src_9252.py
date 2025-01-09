def solve(a, b):
    m, n = len(a), len(b)

    cache = [[0 for __ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[j - 1] == b[i - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    res = ''

    j, i = m, n
    while i > 0 and j > 0:
        if a[j - 1] == b[i - 1]:
            res += a[j - 1]
            i -= 1
            j -= 1
        elif cache[i - 1][j] > cache[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print(cache[n][m])
    print(res[::-1])

    return True


if __name__ == '__main__':
    a = input()
    b = input()
    solve(a, b)
