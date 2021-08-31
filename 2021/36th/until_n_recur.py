import sys

sys.setrecursionlimit(10 ** 5)


def solve_recur(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return solve_recur(n - 10) + solve_recur(n - 5) + solve_recur(n - 3)


def solve_dp(n):
    ar = [0 for _ in range(n + 1)]
    ar[0] = 1

    for i in range(1, n + 1):
        if i - 3 >= 0:
            ar[i] += ar[i - 3]
        if i - 5 >= 0:
            ar[i] += ar[i - 5]
        if i - 10 >= 0:
            ar[i] += ar[i - 10]

    return ar[n]


if __name__ == '__main__':
    n = int(input())
    print(solve_recur(n))
    print(solve_dp(n))
