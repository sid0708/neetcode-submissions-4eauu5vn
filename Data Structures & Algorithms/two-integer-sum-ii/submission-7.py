class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numCache = {}
        for idx, nums in enumerate(numbers):
            m = target - nums
            if m in numCache:
                return [numCache[m],idx+1 ]
            numCache[nums] =idx +1

