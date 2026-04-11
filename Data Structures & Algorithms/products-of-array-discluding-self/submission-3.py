class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calcuate prefix
        n = len(nums)
        pre, post = [0] * n, [0] *n
        pre[0], post[-1] = 1, 1
        res = [0] * n
        for i in range(1, n):
            pre [i]= nums[i-1] * pre[i-1]
        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
        for i in range(n):
            res[i] = pre[i] * post[i]
        return res
        