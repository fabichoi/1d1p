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
