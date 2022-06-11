class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        visited = set()
        res = float("inf")
        
        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    size = abs(x1 - x2) * abs(y1 - y2)
                    res = min(res, size)
            visited.add((x1, y1))
        return res if res != float("inf") else 0
    
    # time complexity: O(n ^ 2)
    # space complexity: O(n)
