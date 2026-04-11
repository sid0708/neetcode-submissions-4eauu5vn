class Solution:
    def rob(self, nums: List[int]) -> int:
        # use recursive
        def dfs(i, cache):
            if cache is None:
                cache = {}
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            else:
                cache[i] = max(nums[i]+ dfs(i+2, cache), dfs(i+1,cache))
            return cache[i]
        return dfs(0,{})
        