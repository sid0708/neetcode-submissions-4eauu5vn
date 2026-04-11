class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals
        intervals.sort(key= lambda x: x[0])
        # create a merged 
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            lastend = merged[-1][1]

            # detect intervals
            if start <= lastend:
                merged[-1][1] = max(end, lastend)
            else:
                merged.append([start, end])
        return merged
