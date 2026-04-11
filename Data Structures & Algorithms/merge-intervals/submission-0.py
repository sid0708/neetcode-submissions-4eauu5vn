class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals, by the start
        intervals.sort(key=lambda x: x[0])
        # create a res []
        res = [intervals[0]]

        for start, end in intervals:
            lastend = res[-1][1]

            # if current start is less than or equal lastsend it's a conflict
            if start <= lastend:
                # update the lastend
                res[-1][1] = max(lastend, end)
            else:
                res.append([start,end])
        return res

        