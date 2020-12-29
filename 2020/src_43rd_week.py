# level2-2
'''
from itertools import combinations

def solution(numbers, target):
    answer = 0
    # nC0, nC1, nC2, nC3, nC4, nCn-1\
    n = len(numbers)
    cnt = 0
    s = sum(numbers)
    for i in range(n):
        for j in combinations([_ for _ in range(n)], i):
            t = s
            for k in j:
                t -= (numbers[k] * 2)
            if t == target:
                cnt += 1

    print(cnt)

    return answer
'''

# level2-1
'''
def solution(nums):
    d = {}
    l = len(nums) // 2
    for num in nums:
        if d.get(num) == None:
            d[num] = 1
        else:
            d[num] += 1
    n = len(d)
    if l < n:
        return l
    return n
'''

# level3-1
'''
def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    while s > 0:
        t = s // n
        answer.append(t)
        s -= t
        n -= 1

    return answer
'''

def solution(n, costs):
    answer = 987654321
    cost = [ [-1 for _ in range(n)] for __ in range(n) ]
    v = [0 for _ in range(n)]
    for c in costs:
        cost[c[0]][c[1]] = c[2]
        cost[c[1]][c[0]] = c[2]

    def dfs(s, e, total_cost, visited):
        if sum(visited) == n:
            return total_cost
        if visited[e] == 1:
            return

        visited[s] = 1
        visited[e] = 1
        total_cost += cost[s][e]
        for i in range(n):
            if i == e:
                continue
            if cost[e][i] != -1:
                return dfs(e, i, total_cost, visited)

    for s in range(n):
        for e in range(n):
            if s == e:
                dfs(s,e,0,v)


    return answer


if __name__ == "__main__":
    print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))




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
'''