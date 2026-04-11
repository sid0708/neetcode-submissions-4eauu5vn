class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # L = 0
        # freq = {}
        # maxFreq, maxLength = 0, 0
        # for R in range(len(s)):
        #     freq[s[R]] = 1+ freq.get(s[R], 0)
        #     maxFreq = max(maxFreq,freq[s[R]] )
        #     while R-L+1 - maxFreq > k:
        #         freq[s[L]] -=1
        #         L +=1
        #     maxLength = max(maxLength, R-L+1)
        # return maxLength
        L ,maxFreq, maxLength= 0,0,0
        freq = {}
        for R in range(len(s)):
            freq[s[R]] = 1 + freq.get(s[R], 0)
            maxFreq = max(maxFreq, freq[s[R]])
            while R - L +1 - maxFreq > k:
                freq[s[L]] -= 1
                L +=1
            maxLength = max(maxLength, R-L+1)
        return maxLength
        






        

    