# BOJ 1063

def solve():
    a, b, n = input().split(' ')
    ax, ay = ord(a[0]) - ord('A') + 1, int(a[1])
    bx, by = ord(b[0]) - ord('A') + 1, int(b[1])
    commands = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1],
                'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
    for _ in range(int(n)):
        cmd_x, cmd_y = commands.get(input())
        x, y = ax + cmd_x, ay + cmd_y
        if x < 1 or x > 8 or y < 1 or y > 8:
            continue
        if x == bx and y == by:
            rx, ry = bx + cmd_x, by + cmd_y
            if rx < 1 or rx > 8 or ry < 1 or ry > 8:
                continue
            bx, by = rx, ry
        ax, ay = x, y

    print(chr(ord('A') + ax - 1) + str(ay))
    print(chr(ord('A') + bx - 1) + str(by))

if __name__ == '__main__':
    solve()
