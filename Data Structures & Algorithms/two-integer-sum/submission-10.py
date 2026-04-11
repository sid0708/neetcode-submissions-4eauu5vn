class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for L in range(len(nums)):
            for R in range(L+1, len(nums)):
                if nums[L] + nums[R] == target:
                    return [L,R]



    
