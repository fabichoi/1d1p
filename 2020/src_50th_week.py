# 50th week

# boj1173
'''
if __name__ == "__main__":
    n, m, M, T, R = map(int, input().split(' '))
    cnt = 0
    now = m

    if m + T > M:
        print(-1)
    else:
        while n > 0:
            if now + T <= M:
                now += T
                n -= 1
            else:
                if now - R >= m:
                    now -= R
                else:
                    now = m

            cnt += 1
        print(cnt)
'''


class boj1236:

    def solve(self, n, m, ar):
        cntX, cntY = 0, 0
        for i in range(n):
            flagY = True
            for j in range(m):
                if ar[i][j] == 'X':
                    flagY = False
            if flagY:
                cntY += 1

        for i in range(m):
            flagX = True
            for j in range(n):
                if ar[j][i] == 'X':
                    flagX = False
            if flagX:
                cntX += 1

        return max(cntY, cntX)


if __name__ == "__main__":
    n, m = map(int, input().split(' '))
    ar = []
    for _ in range(n):
        ar.append(input())

    print(boj1236.solve('', n, m, ar))