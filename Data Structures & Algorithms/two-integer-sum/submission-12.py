class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsIdx = {}
        for idx, value in enumerate(nums):
            numsIdx[value] = idx
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numsIdx and numsIdx[diff] !=i:
                return [i, numsIdx[diff]]
        return []



        