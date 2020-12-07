# 50th week

# boj1173

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