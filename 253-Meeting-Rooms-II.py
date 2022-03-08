"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals):
        res, count = 0, 0
        s, e = 0, 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(count, res)
        return res  
    # time complexity: O(nlogn)
    # space complexity: O(n)
