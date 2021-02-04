def solve(n):
    if int(n ** 0.5) ** 2 == n:
        return 1
    for i in range(1, int((n // 2) ** 0.5) + 1):
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if i ** 2 + j ** 2 == n:
                return 2
            elif (n - i ** 2 - j ** 2) ** 0.5 % 1 == 0:
                return 3
    return 4


print(solve(int(input())))
