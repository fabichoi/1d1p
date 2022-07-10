import math
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost += [0]
        l = len(cost)
        res = [math.inf] * (l + 1)
        res[0] = cost[0]
        res[1] = min(res[0] + cost[1], cost[1])
        for i in range(2, l):
            res[i] = min(res[i - 1] + cost[i], res[i - 2] + cost[i])
        return res[l-1]


s = Solution()
print(s.minCostClimbingStairs([10,15,20]))

'''
from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            cs1, cs2 = False, False
            if i < len(s1) and s1[i] == s3[i + j]:
                cs1 = dfs(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                cs2 = dfs(i, j + 1)
            return cs1 or cs2

        return dfs(0, 0)


s = Solution()
print(s.isInterleave("aabc", "abad", "aabadabc"))

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        lr, rl, res = [1] * l, [1] * l, [1] * l
        for i in range(1, l):
            if ratings[i - 1] < ratings[i]:
                lr[i] = lr[i - 1] + 1
            if ratings[l - i] < ratings[l - i - 1]:
                rl[l - i - 1] = rl[l - i] + 1
        for i in range(l):
            res[i] = max(lr[i], rl[i])
        return sum(res)


s = Solution()
print(s.candy([1, 0, 2]))
'''
