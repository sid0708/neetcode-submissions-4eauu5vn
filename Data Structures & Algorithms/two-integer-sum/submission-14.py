class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsIdx = {}
        for idx, num in enumerate(nums):
            numsIdx[num] = idx
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numsIdx and numsIdx[diff] != i:
                return [i, numsIdx[diff]]
        return []

        