class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_nums = {}
        for idx, value in enumerate(nums):
            complement = target - value
            if complement in target_nums.keys():
                return [target_nums[complement], idx]
            else:
                target_nums[value] =idx
        return []
            
        