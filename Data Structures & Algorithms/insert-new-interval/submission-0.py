class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # there is just one newIntervals
        res = []
        for i in range(len(intervals)):
             # if the new interval comes before the current interval
            if newInterval[1] <intervals[i][0]:
                # append the new interval
                res.append(newInterval)
                # and return in totallity
                return res + intervals[i:]
            # if the new interval comes after the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # there is an overlap
                newInterval = [min(intervals[i][0],newInterval[0] ), max(intervals[i][1],newInterval[1])]
        res.append(newInterval)
        return res


        