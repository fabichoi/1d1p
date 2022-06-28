class Solution:
    def minDeletions(self, s: str) -> int:
        ar = [0 for _ in range(26)]
        res = 0
        for ss in s:
            ar[ord(ss) - ord('a')] += 1
        d = {}
        for a in ar:
            if not a:
                continue
            if not d.get(a):
                d[a] = 1
                continue
            while a:
                a -= 1
                res += 1
                if not d.get(a):
                    d[a] = 1
                    break
        return res


s = Solution()
print(s.minDeletions('ceabaacb'))
