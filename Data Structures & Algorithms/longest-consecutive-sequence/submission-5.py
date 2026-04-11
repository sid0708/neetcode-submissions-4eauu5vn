class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        longest = 0
        numSet = set(nums)
        # check if it's the start of the sequence
        if len(nums) == 0:
            return 0
        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length +=1
                longest = max(length,longest)
        return longest
        