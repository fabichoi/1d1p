# boj 11725

from collections import deque

if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    res = [for _ in range(n + 1)]
    for i in range(n - 1):
        n, m = map(int, input().split(' '))
        tree[n].append(m)
        tree[m].append(n)

    qu = deque()

    while tree[1]:
        t = tree[1].pop(0)
        res[t] = 1
        qu.append(t)

    while qu:
        q = qu.popleft()
        while tree[q]:
            t = tree[q].pop(0)
            res[t] = q
            qu.append(t)



    print(tree)

# test recursion
'''
if __name__ == "__main__":

    def printBin(n):
        if n < 2:
            print(n)
        else:
            printBin(n//2)
            print(n%2)

    printBin(11)
'''

# boj 11729

'''
if __name__ == "__main__":
    n = int(input())


    def hanoi(n, a, b, c):
        if n == 1:
            print(a, c)
        else:
            hanoi(n - 1, a, c, b)
            print(a, c)
            hanoi(n - 1, b, a, c)


    print(2 ** n - 1)
    hanoi(n, 1, 2, 3)
'''

# boj 7576
'''
from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split(' '))
    box = []
    for _ in range(m):
        box.append(list(map(int, input().split(' '))))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    qu = deque()

    for i in range(m):
        for j in range(n):
            if box[i][j] <= 0:
                continue
            qu.append([i, j])

    while qu:
        cy, cx = qu.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if box[ny][nx] == 0:
                box[ny][nx] = box[cy][cx] + 1
                qu.append([ny, nx])

    res = 0
    for i in range(m):
        for j in range(n):
            if box[i][j] == 0:
                print(-1)
                exit(0)
            res = max(res, box[i][j])
    print(res - 1)
'''
