



#boj 1058

'''
if __name__ == "__main__":
    n = int(input())
    rel = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        ar = input()
        for j in range(n):
            if i == j:
                continue
            if ar[j] == "Y":
                rel[i][j] = 1
                rel[j][i] = 1

    res = 0

    for i in range(n):
        q = []
        visited = [0 for _ in range(n)]
        visited[i] = 1
        cnt = 0
        depth = 0

        for j in range(n):
            if i != j and visited[j] == 0 and rel[i][j] == 1:
                q.append([j, depth + 1])

        while True:
            if len(q) < 1:
                break

            cur, depth = q.pop(0)
            if depth > 2:
                continue

            if visited[cur] != 0:
                continue

            cnt += 1
            visited[cur] = 1

            for j in range(n):
                if cur == j:
                    continue
                if rel[cur][j] == 1 and visited[j] == 0:
                    q.append([j, depth + 1])

        res = max(res, cnt)

    print(res)
'''

#boj 2644

'''
if __name__ == "__main__":
    n = int(input())
    s, e = map(int, input().split(' '))
    m = int(input())
    rel = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]
    chon = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split(' '))
        rel[a][b] = rel[b][a] = 1

    q = []
    visited[s] = 1
    chon[s] = 1
    cnt = 0
    for i in range(1, n + 1):
        if s != i:
            if rel[s][i] == 1:
                q.append(i)
                chon[i] = 1
    while True:
        if len(q) == 0:
            break
        cur = q.pop(0)
        cnt += 1
        visited[cur] = 1

        for i in range(1, n + 1):
            if rel[cur][i] == 1 and visited[i] == 0:
                q.append(i)
                chon[i] = chon[cur] + 1
    print(chon[e] if chon[e] > 0 else -1)
'''