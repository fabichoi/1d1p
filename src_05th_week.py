'''
r, b = map(int, input().split(' '))
w = 0
for l in range(1, b+1):
    if b % l != 0:
        continue    
    w = b // l
    sum = w * 2 + l * 2 + 4
    if sum == r:
        if w > l:
            print(str(w + 2) + " " + str(l + 2))
        else:
            print(str(l + 2) + " " + str(w + 2))
        break
'''

'''
t, w = map(int, input().split(' '))
p = [0]
for _ in range(t):
    p.append(int(input()) - 1)
'''

import sys
sys.setrecursionlimit(10**9)

if __name__ == "__main__":
    t, w = map(int, input().split(' '))
    p = [[0, 0]]
    for _ in range(t):
        pp = int(input()) - 1
        p.append([1, 0] if pp == 0 else [0, 1])

    def solve(n, s, c):
        if n == 0:
            return 0
        if c == 0:
            return p[n][s]

        rev_s = 0 if s == 1 else 1

        cur_side = solve(n - 1, s, c) + p[n][s]
        rev_side = solve(n - 1, rev_s, c - 1) + p[n][rev_s]

        return max(cur_side, rev_side)

    print(solve(t, 0, w))

