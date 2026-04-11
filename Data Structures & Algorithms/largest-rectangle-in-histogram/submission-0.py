class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # stores pairs (start_index, height)

        for i, h in enumerate(heights):
            start = i
            # Pop taller bars and calculate area
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index  # extend current bar to the leftmost index of popped bar
            stack.append((start, h))

        # Process remaining bars in stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea