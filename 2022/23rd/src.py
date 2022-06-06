from typing import List


# LCD 51
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = [0] * n
        diag1, diag2 = [0] * (2 * n - 1), [0] * (2 * n - 1)
        res = []

        def boardState():
            rows = []
            for y in column:
                rows.append(((y - 1) * '.') + 'Q' + ((n - y) * '.'))
            return rows

        def search(y):
            if y == n:
                res.append(boardState())
                return
            for x in range(n):
                if column[x] or diag1[x + y] or diag2[x - y + n - 1]:
                    continue
                column[x] = diag1[x + y] = diag2[x - y + n - 1] = y + 1
                search(y + 1)
                column[x] = diag1[x + y] = diag2[x - y + n - 1] = 0

        search(0)
        return res


s = Solution()
print(s.solveNQueens(4))

'''
# LCD 1461
class Solution:
    def hasAllCodes_mine(self, s: str, k: int) -> bool:
        kk = 2 ** k
        ss = set()

        for i in range(len(s)):
            for j in range(i, len(s) - k + 1):
                temp = int('0b' + s[i:i+k], 2)
                ss.add(temp)

        ss = sorted(ss)

        for i in range(kk):
            if i != ss[i]:
                return False

        return True

    def hasAllCodes(self, s: str, k: int) -> bool:
        got = {s[i - k:i] for i in range(k, len(s) + 1)}
        return len(got) == 1 << k

s = Solution()
print(s.hasAllCodes("0110", 2))
'''
