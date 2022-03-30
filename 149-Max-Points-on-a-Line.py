class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            lookup = {}
            tmp = 0
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if (x1 - x2) == 0:
                    slope = 0
                elif (y1- y2) == 0:
                    slope = float("inf")
                else:
                    slope = (y2 - y1) / (x2 - x1)
                if slope in lookup:
                    lookup[slope] += 1
                else:
                    lookup[slope] = 1
                tmp = max(tmp, lookup[slope])
            res = max(res, tmp)
        return res + 1
      
      # time complexity: O(n^2)
      # space complexity: O(n)
