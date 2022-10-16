class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minHeap = [(0, 0, 0)] # cnt, row, col
        
        while minHeap:
            cnt, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            if r == m - 1 and c == n - 1:
                return cnt
            visited.add((r, c))
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if 0 <= newR < m and 0 <= newC < n and (newR, newC) not in visited:
                    heapq.heappush(minHeap, (max(cnt, abs(heights[newR][newC] - heights[r][c])), newR, newC))
