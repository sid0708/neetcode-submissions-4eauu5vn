class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        res = [0] * len(temp)
        stack = []

        for idx,t in enumerate(temp):
            while stack and stack[-1][0]<t:
                idx_t, idx_i = stack.pop()
                res[idx_i] = idx - idx_i
            stack.append((t,idx))
        return res
        