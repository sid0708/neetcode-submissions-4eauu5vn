class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        subset, currset = [], []
        self.helper(0, nums, currset,subset)
        return subset
    def helper(self,i, nums, currset,subset):
        if i >= len(nums):
            subset.append(currset.copy())
            return
        # include nums[i]
        currset.append(nums[i])
        self.helper(i+1, nums, currset,subset)
        # skip all elements
        currset.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i +=1
        self.helper(i+1, nums, currset,subset)
        
        

        