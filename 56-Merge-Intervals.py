class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
          return intervals
        
        # intervals.sort(key = lambda i : i[0])
        intervals.sort()
        output = [intervals[0]]
        for start, end in intervals[1:]:
            prevEnd = output[-1][1]
            if start <= prevEnd:
                output[-1][1] = max(prevEnd, end)
            else:
                output.append([start, end])
        return output
    
    # time complexity: O(nlogn)
    # space complexity: O(n)
