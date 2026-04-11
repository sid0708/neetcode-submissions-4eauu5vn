class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            count = {}
            length = 0
            maxf = 0
            L = 0
            
            for R in range(len(s)):
                count[s[R]] = 1 + count.get(s[R], 0)
                # compute max freq
                maxf = max(maxf,count[s[R]])
                # the trick if that the valid needs substring -maxf to be less or equal to k
                # if it's more than resize the window
                while (R-L+1) - maxf >k:
                    # resize by removing the count of L
                    count[s[L]] -=1
                    # Also, once you remove it increment the L
                    L +=1
                length = max(length, R - L+1)
            return length

        