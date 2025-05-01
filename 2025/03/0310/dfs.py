from collections import defaultdict


if __name__ == '__main__':
    assert (solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A')
            == ['A', 'B', 'C', 'D', 'E'])
    assert (solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A')
            == ['A', 'B', 'D', 'E', 'F', 'C'])
