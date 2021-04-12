# Codeforces Round  693 (Div. 3)
# No.1

'''
if __name__ == "__main__":
    for _ in range(int(input())):
        res = 1
        w, h, n = map(int, input().split(' '))
        while True:
            if w % 2:
                break
            w //= 2
            res *= 2
        while True:
            if h % 2:
                break
            h //= 2
            res *= 2
        print("YES" if res >= n else "NO")
'''

# No.2
'''
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split(' ')))
        if (a.count(1) % 2) or (a.count(2) % 2):
            print("NO")
        else:
            print("YES")
'''


# boj 11660

from sys import stdin

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split(' '))
    ar = [[0 for _ in range(n+1)]]
    for __ in range(n):
        ar.append([0] + list(map(int, stdin.readline().split(' '))))

    sar = [[0 for _ in range(n+1)] for __ in range(n+1)]
    for y in range(1, n+1):
        for x in range(1, n+1):
            sar[y][x] = ar[y][x] + sar[y][x-1] + sar[y-1][x] - sar[y-1][x-1]

    results = ''
    for __ in range(m):
        i, j, k, l = map(int, stdin.readline().split(' '))
        result = sar[k][l] - sar[i-1][l] - sar[k][j-1] + sar[i-1][j-1]
        results += str(result) + '\n'

    print(results)
