class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxfreq, maxLen = 0, 0
        L = 0
        for R in range(len(s)):
            freq[s[R]] = 1+ freq.get(s[R], 0)
            maxfreq = max(maxfreq, freq[s[R]])
            while R-L+1 - maxfreq > k:
                freq[s[L]] -=1
                L += 1
            maxLen = max(maxLen, R-L+1)
        return maxLen


