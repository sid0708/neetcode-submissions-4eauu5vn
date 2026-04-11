class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for n in nums:
            if n-1 not in nums:
                current_length =1

                while n+current_length in nums:
                    current_length +=1
                    
                max_length = max(current_length, max_length)
        return max_length
 
            

      
        