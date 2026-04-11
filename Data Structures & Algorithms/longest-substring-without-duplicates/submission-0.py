class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        res = 0
        charset = set()

        for R in range(len(s)):
            while s[R] in charset:
                # continue removing the chars
                charset.remove(s[L])
                L += 1
            charset.add(s[R])
            res = max(res, R-L+1)
        return res


        