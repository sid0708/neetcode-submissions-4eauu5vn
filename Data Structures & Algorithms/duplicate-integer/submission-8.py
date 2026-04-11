class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) != len(set(nums)):
            return True
        return False
        