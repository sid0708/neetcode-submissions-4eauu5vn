class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cache = {}
        L, maxf,res = 0,0,0
        for R in range(len(s)):
            # in cache
            cache[s[R]] = 1 +cache.get(s[R], 0)
            maxf = max(maxf,cache[s[R]])
            while(R-L+1) - maxf >k:
                cache[s[L]] -=1
                L +=1
            res = max(res, R-L+1)
        return res


        

    