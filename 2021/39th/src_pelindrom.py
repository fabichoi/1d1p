import sys

sys.setrecursionlimit(10 ** 5)


def solve(s, start, end):
    if start > end:
        return 0
    if start == end:
        return 1

    if s[start] == s[end]:
        return solve(s, start + 1, end - 1) + 2
    else:
        left = solve(s, start, end - 1)
        right = solve(s, start + 1, end)
        return left if left > right else right


if __name__ == '__main__':
    s = input()
    print(solve(s, 0, len(s) - 1))
