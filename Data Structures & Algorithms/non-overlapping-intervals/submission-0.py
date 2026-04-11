class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
            # sort by end time
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # overlap → remove this interval
                count += 1
            else:
                # no overlap → update end
                prev_end = end

        return count