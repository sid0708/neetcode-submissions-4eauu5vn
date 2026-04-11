class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length, maxLength = 0,0
        L = 0
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                length -=1
                L +=1
            seen.add(s[R])
            length +=1
            maxLength = max(length,maxLength )
        return maxLength


