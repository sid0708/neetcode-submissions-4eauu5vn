class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currset, subset = [], []
        self.helper(0, nums, currset,subset)
        return subset
    def helper(self,i, nums, currset,subset):
        if i>=len(nums):
            subset.append(currset.copy())
            return
        # include i
        currset.append(nums[i])
        self.helper(i+1, nums, currset,subset)
        # don't include i
        currset.pop()
        self.helper(i+1, nums, currset,subset)
        