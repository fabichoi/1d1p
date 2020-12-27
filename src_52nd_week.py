# 52nd week

if __name__ == "__main__":
    n = int(input())
    mod_n = 9901

    d = [0 for _ in range(n + 1)]
    dc1 = [1 for _ in range(n + 1)]
    dc2 = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        dc1[i] = (dc1[i - 1] + dc2[i - 1]) % mod_n
        dc2[i] = (2 * dc1[i - 1] + dc2[i - 1]) % mod_n
        d[i] = (dc1[i] + dc2[i]) % mod_n

    print(d[n])