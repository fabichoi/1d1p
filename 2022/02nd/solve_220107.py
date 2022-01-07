# BOJ 1024
import itertools

def solve():
    # a, b = map(int, input().split(' '))
    a = [x + 1 for x in range(1000000000)]
    b = list(itertools.accumulate(a))


if __name__ == '__main__':
    solve()


