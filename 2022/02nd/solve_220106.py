# BOJ 1009
def solve():
    ar = [ [10, 10, 10, 10], [1, 1, 1, 1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6, 4, 6], [5, 5, 5, 5], [6, 6, 6, 6],
        [7, 9, 3, 1], [8, 4, 2, 6], [9, 1, 9, 1] ]

    for _ in range(int(input())):
        a, b = map(int, input().split(' '))
        print(ar[a % 10][b % 4 - 1])

if __name__ == '__main__':
    solve()
