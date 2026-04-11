class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calcuate prefix
        n =len(nums)
        pre, post = [0] * n, [0]*n
        res = [1] *n
        pre[0], post[-1] = 1, 1

        for i in range(1,n):
            pre[i] = nums[i-1] *pre[i-1]
        for i in range(n-2, -1,-1 ):
            post[i] = nums[i+1] * post[i+1]
        for j in range(n):
            res[j] = pre[j] * post[j]
        return res
        