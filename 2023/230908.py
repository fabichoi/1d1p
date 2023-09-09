from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ar = [[], [1], [1, 1]]
        for i in range(3, 31):
            a = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    a.append(1)
                    continue
                a.append(ar[i - 1][j - 1] + ar[i - 1][j])
            ar.append(a)
        return ar[numRows]


s = Solution()
print(s.generate(30))
