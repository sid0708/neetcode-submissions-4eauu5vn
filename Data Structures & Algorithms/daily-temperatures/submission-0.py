class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        result = [0] * len(temp)
        stack = []
        for idx, tmp in enumerate(temp):
            # see the youtube video
            while stack and stack[-1][0] < tmp:
                # pop both index and elment
                stack_t, stack_i = stack.pop()
                result[stack_i] = idx - stack_i
            stack.append((tmp, idx))
        return result
        