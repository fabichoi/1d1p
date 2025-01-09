import copy
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        a = copy.deepcopy(cardPoints)
        b = copy.deepcopy(cardPoints)
        l = len(cardPoints)
        if l == k:
            return sum(cardPoints)

        for i in range(1, l):
            a[i] += a[i - 1]
            b[l - i - 1] += b[l - i]

        res = max(a[k - 1], b[-k])
        for i in range(0, k - 1):
            res = max(res, a[i] + b[(l-(k-i-1))])

        return res


s = Solution()
print(s.maxScore(cardPoints=[100, 40, 17, 9, 73, 75], k=3))

'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        rsorted = sorted(nums, reverse=True)
        count = 0
        for i in range(len(nums)):
            if nums[i] != rsorted[i]:
                count += 1
            if count > 2:
                break
        return True if count == 2 else False


s = Solution()
print(s.checkPossibility(nums=[9, 3, 5]))


import heapq
from typing import List


# LCD 1354
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heapq._heapify_max(target)
        s = sum(target)

        while target[0] != 1:
            sub = s - target[0]
            if sub == 0:
                return False

            n = max((target[0] - 1) // sub, 1)
            s -= n * sub

            target0 = target[0] - n * sub
            if target0 < 1:
                return False

            heapq._heapreplace_max(target, target0)

        return True


s = Solution()
print(s.isPossible(target=[9, 3, 5]))
'''
