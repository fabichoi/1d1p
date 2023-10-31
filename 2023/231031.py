from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        res = []
        for v in arr:
            k = bin(v).count('1')
            if not d.get(k):
                d[k] = [v]
                continue
            d[k].append(v)
        d = sorted(d.items())
        for dd in d:
            res.extend(sorted(dd[1]))
        return res

s = Solution()
print(s.sortByBits(arr=[10, 100, 1000, 10000]))
