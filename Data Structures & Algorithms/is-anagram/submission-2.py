class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        if len(s) != len(t):
            return False
        for idx in range(len(s)):
            if s[idx] != t[idx]:
                return False
        return True
        
        
        