from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        gr = defaultdict(list)

        for x, y in adjacentPairs:
            gr[x].append(y)
            gr[y].append(x)

        root = None
        for n in gr:
            if len(gr[n]) == 1:
                root = n
                break

        def dfs(node, prev, ans):
            ans.append(node)
            for nei in gr[node]:
                if nei != prev:
                    dfs(nei, node, ans)

        ans = []
        dfs(root, None, ans)
        return ans

s = Solution()
print(s.restoreArray([[2, 1], [3, 4], [3, 2]]))
