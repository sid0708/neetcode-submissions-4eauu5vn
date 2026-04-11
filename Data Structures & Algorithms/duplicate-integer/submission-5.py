class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for each in nums:
            if each not in seen:
                seen.add(each)
            else:
                return True
        return False