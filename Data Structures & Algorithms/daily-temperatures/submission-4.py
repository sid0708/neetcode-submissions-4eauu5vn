class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        temp = temperatures
        n = len(temp)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:
                poped_idx = stack.pop()
                res[poped_idx]  = i - poped_idx
            stack.append(i)
        return res


