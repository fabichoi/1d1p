# boj 1012
'''
import sys
sys.setrecursionlimit(10 ** 6)

if __name__ == "__main__":
    ts = int(input())

    for t in range(ts):
        m, n, k = map(int, input().split(' '))
        board = [[0 for _ in range(m)] for __ in range(n)]
        visited = [[0 for _ in range(m)] for __ in range(n)]

        for _ in range(k):
            a, b = map(int, input().split(' '))
            board[b][a] = 1

        cnt = 1


        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if board[y][x] == 0:
                return
            if visited[y][x] != 0:
                return

            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]

            visited[y][x] = cnt

            for i in range(4):
                dfs(x + dx[i], y + dy[i])

            return 1


        for y in range(n):
            for x in range(m):
                if dfs(x, y) is not None:
                    cnt += 1

        print(cnt - 1)
'''
# boj 10164
'''
if __name__ == "__main__":
    n, m, k = map(int, input().split(' '))
    nm = 16
    board = [[1 for _ in range(nm)] for __ in range(nm)]

    for i in range(1, nm):
        for j in range(1, nm):
            board[j][i] = board[j - 1][i] + board[j][i - 1]

    tx = m
    ty = n
    if k != 0:
        ty = (k - 1) // m
        tx = (k - 1) % m

    if k == 0:
        print(board[n - 1][m - 1])
    else:
        print(board[n - ty - 1][m - tx - 1] * board[ty][tx])

'''
#boj 2583
'''
import sys

sys.setrecursionlimit(100000)

if __name__ == "__main__":
    m, n, k = map(int, input().split(' '))
    board = [[0 for _ in range(n + 2)] for __ in range(m + 2)]
    for i in range(n + 2):
        board[0][i] = -1
        board[m + 1][i] = -1
    for j in range(m + 2):
        board[j][0] = -1
        board[j][n + 1] = -1

    for i in range(k):
        x1, y1, x2, y2 = map(int, input().split(' '))
        for x in range(x1 + 1, x2 + 1):
            for y in range(y1 + 1, y2 + 1):
                board[y][x] = -1

    cnt = 1
    area = 1
    areas = []


    def dfs(x, y):
        if board[y][x] != 0:
            return
        global cnt
        global area

        board[y][x] = cnt

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            if dfs(x + dx[i], y + dy[i]) is not None:
                area += 1

        return cnt


    for y in range(1, m + 2):
        for x in range(1, n + 2):
            area = 1
            res = dfs(x, y)
            if res is not None:
                areas.append(area)
                cnt += 1
    cnt -= 1
    areas.sort()
    print(str(cnt) + "\n" + " ".join(map(str, areas)))
'''