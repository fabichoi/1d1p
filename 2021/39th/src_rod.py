def solve_dp(v, n):
    cache = [0 for _ in range(n+1)]

    for i in range(1, n + 1):
        cache[i] = -987654321

        for j in range(1, i + 1):
            cache[i] = max(cache[i], v[j] + cache[i - j])

    return cache[n]


if __name__ == '__main__':
    v = [0] + list(map(int, input().split()))
    print(solve_dp(v, len(v) - 1))
