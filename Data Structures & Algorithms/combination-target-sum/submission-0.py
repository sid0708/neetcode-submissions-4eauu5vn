class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        if len(nums) == 0:
            return []
        self.sumhelper(0,[], combs, nums,target )
        return combs
    def sumhelper(self,i,currcombs,combs,nums, target ):
        if sum(currcombs) == target:
            combs.append(currcombs.copy())
            return
        if i >= len(nums) or sum(currcombs) > target:
            return
        # include i
        currcombs.append(nums[i])
        self.sumhelper(i, currcombs,combs,nums, target)
        currcombs.pop()
        self.sumhelper(i+1, currcombs,combs,nums, target)

        
        