class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R =0
        seen =set()
        length = 0
        while R < len(s):
            if s[R] not in seen:
                seen.add(s[R])
                length = max(length, R - L + 1)
                R +=1
            elif s[R] in seen:
                seen.remove(s[L])
                L +=1
        return length


                

