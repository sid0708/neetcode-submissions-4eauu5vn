class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] *26
        want = [0] *26
        k = len(s1)

        for c in s1:
            need[ord(c)-97] +=1
        
        for i, c in enumerate(s2):
            want[ord(c) -97] +=1
            if i >=k:
                want[ord(s2[i-k]) -97] -=1
            if need ==want:
                return True
        return False
