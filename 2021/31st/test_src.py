# BOJ 2670
import sys


def solve(n, ar):
    for i in range(1, n):
        m = ar[i - 1] * ar[i]
        ar[i] = max(m, ar[i])

    return max(ar)


def test_solve():
    n = 8
    ar = [1.1, 0.7, 1.3, 0.9, 1.4, 0.8, 0.7, 1.4]
    assert "{:.3f}".format(solve(n, ar)) == "1.638"


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    ar = []
    for i in range(n):
        ar.append(float(sys.stdin.readline()))
    print("{:.3f}".format(solve(n, ar)))
