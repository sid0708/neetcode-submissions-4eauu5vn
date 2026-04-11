class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet =set(nums)
        current_length = 0
        maxLength = 0
        for n in numSet:
            if (n-1) not in numSet: 
                current_length = 0
                while (n+current_length) in numSet:
                    current_length +=1
                maxLength = max(maxLength, current_length)
        return maxLength
        
        

      
        