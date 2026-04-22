class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the events based on end time
        intervals.sort(key= lambda x: x[1])
        count = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            # conflict
            if start < prev_end:
                count +=1
            else:
                prev_end = end
        return count




