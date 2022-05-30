class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        res = -1
        lst = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        q = deque()
        q.append([0, 0, k, 0])
        
        while(q):
            r, c, left, steps = q.popleft()
            if r == m - 1 and c == n - 1:
                res = steps
                return res
            
            if grid[r][c] == 1:
                if left == 0:
                    continue
                left -= 1

            for x, y in lst:
                newR, newC = r + x, c + y
                if 0 <= newR < m and 0 <= newC < n and (newR, newC, left) not in visited:
                    q.append([newR, newC, left, steps + 1])
                    visited.add((newR, newC, left))
        return res
