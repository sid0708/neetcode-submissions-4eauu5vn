class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        # create freq counter
        a = [0] * 26
        b = [0] * 26
        # fill the freq counter
        for i in range(m):
            a[ord(s1[i]) - ord('a')] += 1
            b[ord(s2[i]) - ord('a')] += 1
        # check if the freq count are equal
        if a == b:
            return True
        for i in range(m, n):
            b[ord(s2[i]) - ord('a')] += 1
            b[ord(s2[i - m]) - ord('a')] -= 1
            if a == b:
                return True

        return False
