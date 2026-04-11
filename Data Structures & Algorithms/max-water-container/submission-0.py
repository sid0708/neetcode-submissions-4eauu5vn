class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_area = 0
        max_area = 0
        # Initialize left,
        # to get maximum width
        L = 0
        R = len(heights) -1

        # use the two pointer method
        while L < R:
            # compute area, width * height
            # the bottlneck is height smallest of
            # left pointer and right pointer
            width = (R - L)
            min_heights = min(heights[R], heights[L])
            current_area = width * min_heights
            max_area = max(current_area, max_area)
            if heights[L] <= heights[R]:
                # then get new bigger heigt
                L +=1
            else:
                R -=1
        return max_area
     