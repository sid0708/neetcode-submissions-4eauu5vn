class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset =set(nums)
        length, maxlength = 0,0
        for num in nums:
            if (num-1) not in nums:
                length = 1
                while (num+length) in nums:
                    length +=1
                maxlength = max(maxlength, length)
        return maxlength
    

   

                
        


        