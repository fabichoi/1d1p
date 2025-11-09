from collections import defaultdict, deque

def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    queue, visited, result = deque([start]), set(), list()
    visited.add(start)
    result.append(start)

    while queue:
        node = queue.popleft()
        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                result.append(neighbor)
                queue.append(neighbor)

    return result

if __name__ == '__main__':
    assert (solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)], 1)
            == [1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert (solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1)
            == [1, 2, 3, 4, 5, 0])
