# boj 2170

from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())
    res = 0
    ar = []
    for _ in range(n):
        ar.append(list(map(int, stdin.readline().split(' '))))
    ar.sort(key=lambda x : (x[0], x[1]))

    ma, mb = ar[0][0], ar[0][1]
    for i in range(1, n):
        a, b = ar[i][0], ar[i][1]
        if ma <= a and mb >= b:
            continue

        if mb < a:
            res += mb - ma
            ma = a
            mb = b
        else:
            ma = min(ma, a)
            mb = max(mb, b)

    res += mb - ma
    print(res)
