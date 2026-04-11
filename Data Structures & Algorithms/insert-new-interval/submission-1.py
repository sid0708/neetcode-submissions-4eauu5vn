class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # Case 1: new interval comes before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # Case 2: new interval comes after current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # Case 3: overlap → merge
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        
        # If newInterval is after all intervals
        res.append(newInterval)
        return res