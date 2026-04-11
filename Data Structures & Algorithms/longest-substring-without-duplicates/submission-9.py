class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        seen = set()
        maxLength = 0
        for R in range(len(s)):
            while s[R] in seen: # keep on shrinking 
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            maxLength = max(maxLength, R - L + 1)
        return maxLength


