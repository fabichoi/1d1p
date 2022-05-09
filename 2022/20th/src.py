# BOJ 4419
n = int(input())
bs, c = [], ['']
for _ in range(n):
    c.append(input().rstrip())

nb = 0
for _ in range(1000):
    try:
        bs.append(list(map(int, input().split())))
        nb += 1
    except EOFError:
        break

eliminated = [False for _ in range(n + 1)]
while True:
    vote = [0 for _ in range(n + 1)]

    for b in bs:
        while True:
            if not eliminated[b[0]]:
                break
            b.pop(0)
        vote[b[0]] += 1

    max_v = max(vote[1:])

    if max_v >= nb / 2:
        for i in range(1, n + 1):
            if vote[i] == max_v:
                print(c[i])
        break

    min_v = 1000
    for i in range(1, n + 1):
        if eliminated[i]:
            continue
        if min_v > vote[i]:
            min_v = vote[i]

    if max_v == min_v:
        for i in range(1, n + 1):
            if vote[i] == max_v:
                print(c[i])
        break

    for i in range(1, n + 1):
        if vote[i] == min_v:
            eliminated[i] = True
