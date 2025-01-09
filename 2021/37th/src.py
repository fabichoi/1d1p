import sys

sys.setrecursionlimit(10 ** 5)


def solve(a, b, c):
    la, lb, lc = len(a), len(b), len(c)
    if la == 0 and lb == 0 and lc == 0:
        return True
    if la + lb != lc:
        return False

    case1, case2 = False, False

    if la != 0 and a[0] == c[0]:
        case1 = solve(a[1:], b, c[1:])

    if lb != 0 and b[0] == c[0]:
        case2 = solve(a, b[1:], c[1:])

    return case1 or case2


if __name__ == '__main__':
    a, b, c = input().split()
    print(solve(a, b, c))
