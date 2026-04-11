class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        area, maxArea = 0, 0
        while L <R:
            area = min(heights[R], heights[L]) *(R - L)
            maxArea = max(area, maxArea)
            if heights[L] <heights[R]:
                L +=1
            else:
                R -=1
        return maxArea

        