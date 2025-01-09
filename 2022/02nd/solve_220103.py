# BOJ 1002
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))
    d = pow(x2 - x1, 2) + pow(y2 - y1, 2)
    answer = -1

    if pow(r2 - r1, 2) < d < pow(r2 + r1, 2):
        answer = 2
    elif pow(r1 + r2, 2) == d or pow(r2 - r1, 2) == d:
        answer = 1
    elif pow(r1 + r2, 2) < d or pow(r2 - r1, 2) > d:
        answer = 0

    if x1 == x2 and y1 == y2 and r1 == r2:
        answer = -1

    print(answer)