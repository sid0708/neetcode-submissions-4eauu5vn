class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        a = [0] * 26  # counts for s1
        b = [0] * 26  # counts for current window in s2

        # initialize counts for s1 and the first window of s2
        for i in range(m):
            a[ord(s1[i]) - ord('a')] += 1
            b[ord(s2[i]) - ord('a')] += 1

        # check the first window
        if a == b:
            return True

        # slide the window over s2
        for i in range(m, n):
            b[ord(s2[i]) - ord('a')] += 1           # add new char
            b[ord(s2[i - m]) - ord('a')] -= 1       # remove old char
            if a == b:
                return True

        return False