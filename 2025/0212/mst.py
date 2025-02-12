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




if __name__ == '__main__':
    assert solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4
