from collections import defaultdict


def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    visited, result = set(), list()

    def dfs(node, visited, result):
        visited.add(node)
        result.append(node)

        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, visited, result)

    dfs(start, visited, result)
    return result


if __name__ == '__main__':
    assert (solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A')
            == ['A', 'B', 'C', 'D', 'E'])
    assert (solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A')
            == ['A', 'B', 'D', 'E', 'F', 'C'])
