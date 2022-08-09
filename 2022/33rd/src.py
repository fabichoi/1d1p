from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums.pop(0)]
        for num in nums:
            if num > arr[-1]:
                arr.append(num)
            else:
                # arr[bisect_left(arr, num)] = num
                for i in range(len(arr)):
                    if arr[i] >= num:
                        arr[i] = num
                        break
        return len(arr)


s = Solution()
print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))
