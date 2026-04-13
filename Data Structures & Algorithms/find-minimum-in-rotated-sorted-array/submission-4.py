class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) -1
        while L <R:
            mid = (L+R)//2
            # if mid is in first half
            if nums[mid] > nums[R]:
               L = mid +1
            # if mid is lower half
            elif nums[mid] < nums[R]:
                R = mid
        return nums[L]
