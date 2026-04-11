class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        target = [0] * 26  # counts for s1
        window = [0] * 26  # counts for current window in s2

        # initialize counts for s1 and the first window of s2
        for i in range(m):
            target[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        # check the first window
        if target == window:
            return True

        # slide the window over s2
        for i in range(m, n):
            window[ord(s2[i]) - ord('a')] += 1           # add new char
            window[ord(s2[i - m]) - ord('a')] -= 1       # remove old char
            if target == window:
                return True

        return False
