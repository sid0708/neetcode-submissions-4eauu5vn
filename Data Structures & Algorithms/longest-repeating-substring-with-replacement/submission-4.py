class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf, L = 0, 0
        maxl =0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxf = max(maxf, count[s[R]])
            # breached condition
            while (R-L+1) - maxf > k:
                count[s[L]] -= 1
                L +=1
            maxl = max(maxl, R-L+1)
        return maxl
    
        
              
        