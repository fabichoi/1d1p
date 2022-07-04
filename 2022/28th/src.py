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
