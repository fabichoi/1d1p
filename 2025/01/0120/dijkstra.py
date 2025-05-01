import heapq

def solution(graph, start):
    distances =

if __name__ == '__main__':
    assert (solution({'A': {'B': 9, 'C': 3}, 'B': {'A': 5}, 'C': {'B': 1}}, 'A')
            == [{'A': 0, 'B': 4, 'C': 3},
                {'A': ['A'], 'B': ['A', 'C', 'B'], 'C': ['A', 'C']}])
    assert (solution({'A': {'B': 1}, 'B': {'C': 5}, 'C': {'D': 1}, 'D': {}}, 'A')
            == [{'A': 0, 'B': 1, 'C': 6, 'D': 7},
                {'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'B', 'C'], 'D': ['A', 'B', 'C', 'D']}])
