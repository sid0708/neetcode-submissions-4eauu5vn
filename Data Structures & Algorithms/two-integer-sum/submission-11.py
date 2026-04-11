class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cacheSum = {} # num: idx
        for idx, each in enumerate(nums):
            diff = target - each
            if diff in cacheSum and idx!=cacheSum[diff]:
                return [cacheSum[diff],idx]
            cacheSum[each] = idx
        return []


    




    
