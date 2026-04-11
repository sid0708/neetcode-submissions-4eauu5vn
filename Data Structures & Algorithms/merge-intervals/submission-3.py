class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on start times
        intervals.sort(key=  lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastend = res[-1][1]
            # if current start is less than lastend
            if start <= lastend:
                # conflicts
                res[-1][1] = max(lastend, end)
            else:
                res.append([start, end])
        return res
