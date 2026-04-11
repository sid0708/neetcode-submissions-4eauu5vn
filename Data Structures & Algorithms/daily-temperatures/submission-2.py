class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        stack = [] #(temp, idx)
        temp = temperatures
        res = [0] * len(temp)
        for i, t in enumerate(temp):
            while stack and t> stack[-1][0]:
                # pop the element
                stackt, stacki = stack.pop()
                # no fill the res
                res[stacki] = i-stacki
            stack.append((t,i))
        return res


