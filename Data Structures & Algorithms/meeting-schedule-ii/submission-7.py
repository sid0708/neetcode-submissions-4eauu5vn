"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        # sort by start and end times
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        # now for room
        count, res = 0, 0
        # for the index of the start and end pointers
        s, e = 0, 0
        # traverse over the start
        while s <len(intervals):
            # if the end is greater than start of pairwise
            if start[s] < end[e]:
                s +=1
                count +=1
            else:
                e +=1
                count -=1
            # at each iteration the maximum number of room need to be computed
            res = max(res, count)
        return res
        




        