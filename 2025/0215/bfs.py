from collections import defaultdict, deque


if __name__ == '__main__':
    assert (solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)], 1)
            == [1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert (solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1)
            == [1, 2, 3, 4, 5, 0])
