# boj 6186

def solve():
    r, c = map(int, input().split(' '))
    str = ''.join('.' for _ in range(c+2))
    ar = [str]
    for _ in range(r):
        ar.append('.' + input() + '.')
    # (visited 배열도 필요함)
    ar += [str]
    visited = [[0 for _ in range(c+2)] for __ in range(r+2)]
    cnt = 1

    '''
    dfs 함수 선언
    cnt는 1
    visited[y][x]가 0일 경우,
    1,1부터 순회하면서
    (x-1, y), (x+1, y), (x, y-1), (x, y+1)
    인 경우 visited[y][x] = cnt를 수행
    다시 dfs 불러 들임
    사방을 둘러봤는데 아무것도 걸리는게 없으면
    return
    순회의 끝에는 cnt += 1
    '''

    def dfs(x, y):
        if visited[y][x] == 0:
            if ar[y][x] == '#':
                visited[y][x] = cnt
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
                return 1
        return 0

    for y in range(1, r+1):
        for x in range(1, c+1):
            cnt += dfs(x, y)

    print(cnt-1)

if __name__ == "__main__":
    solve()