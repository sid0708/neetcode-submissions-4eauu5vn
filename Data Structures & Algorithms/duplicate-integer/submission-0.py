class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()
        for each in nums:
            if each not in uniqueSet:
                uniqueSet.add(each)
        if len(uniqueSet) == len(nums):
            return False
        return True