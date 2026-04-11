from collections import Counter # imported counter 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if s1 == s2:
            return True
        l=0
        length = len(s1)
        while l<=len(s2) -length:
            if Counter(s1) == Counter(s2[l:l+length]):
                return True
            else:
                l+=1
        return False