class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        R = 0
        freq = {}
        maxCount = 0
        res =0
        for R in range(len(s)):
            count = 1+ freq.get(s[R], 0)
            freq[s[R]] = count
            maxCount = max(maxCount, count)
            while(R-L+1) - maxCount > k:
                freq[s[L]] -= 1
                L += 1
            res = max(R-L+1,res)
        return res

            
