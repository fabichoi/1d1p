# BOJ 1333
def solve():
    n, l, d = map(int, input().split(' '))
    ar = []
    music = [1 for _ in range(l)] + [0, 0, 0, 0, 0]
    for i in range(1, n + 1):
        ar += music
    pos = 0
    ar += [0 for _ in range(n+1)]
    while pos < len(ar):
        if ar[pos] == 0:
            break
        pos += d
    return pos

print(solve())
