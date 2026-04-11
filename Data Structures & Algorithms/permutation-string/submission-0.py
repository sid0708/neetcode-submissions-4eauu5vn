class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # start with the length
        n1 = len(s1)
        n2 = len(s2)
        # edge case
        if n1 > n2:
            return False
        # create a frequency list
        s1Freq = [0] * 26
        s2Freq = [0] *26
        # now update it
        for i in range(n1):
            s1Freq[ord(s1[i]) -97] += 1
            s2Freq[ord(s2[i]) -97] += 1
        # ideal case both are equal
        if s1Freq == s2Freq:
            return True
        # if now then do the following
        for i in range(n1, n2):
            # move the pointer and add
            s2Freq[ord(s2[i]) -97] += 1
            # also remove the first element
            s2Freq[ord(s2[i-n1]) - 97] -=1
            if s1Freq == s2Freq:
                return True
        return False

        