class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # store the result here
        result = [1] * len(nums)
        # initialize prefix as 1
        prefix = 1
        # forward pass prefix
        for i in range(len(nums)):
            result[i] = prefix
            # calculate running prefix
            prefix *= nums [i]
        # back pass suffix
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            # multiply prefix by suffix
            result[i] *= suffix
            # calcualte running suffix
            suffix *= nums[i]
        return result

        

        

        