from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            num = nums[l[i]:r[i]+1]
            num.sort()
            if len(num) < 2:
                result.append(True)
                continue
            diff = num[1] - num[0]
            is_found = False
            for j in range(len(num) - 1):
                if num[j + 1] - num[j] != diff:
                    result.append(False)
                    is_found = True
                    break
            if not is_found:
                result.append(True)
        return result


s = Solution()
nums = [4, 6, 5, 9, 3, 7]
l = [0, 0, 2]
r = [2, 3, 5]
print(s.checkArithmeticSubarrays(nums, l, r))
