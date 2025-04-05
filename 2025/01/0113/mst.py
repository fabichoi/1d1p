def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot, yroot = find(parent, x), find(parent, y)

    if rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
        return
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
        return
    parent[yroot] = xroot
    rank[xroot] += 1


def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent, rank = [i for i in range(n)], [0 for _ in range(n)]
    min_cost, edges = 0, 0

    for edge in costs:
        if edges == n - 1:
            break
        x, y = find(parent, edge[0]), find(parent, edge[1])

        if x != y:
            union(parent, rank, x, y)
            min_cost += edge[2]
            edges += 1

    return min_cost


if __name__ == '__main__':
    assert solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4
