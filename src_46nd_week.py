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