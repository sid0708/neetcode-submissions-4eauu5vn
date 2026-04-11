class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        maxArea = 0
        R = len(heights) -1
        # area = 1/2*min(height)*(length)
        while L <R:
            h = min(heights[L], heights[R])
            w = R-L
            maxArea = max(maxArea, h*w)
            if heights[L] >heights[R]:
                R -=1
            else:
                L +=1
        return maxArea


     