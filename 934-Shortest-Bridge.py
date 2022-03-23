class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
                return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        def bfs():
            res = 0
            q = deque(visited)
            
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        newR = row + dr
                        newC = col + dc
                        if newR < 0 or newC < 0 or newR >= len(grid) or newC >= len(grid[0]) or (newR, newC) in visited:
                            continue
                        if grid[newR][newC] == 1:
                            return res
                        visited.add((newR, newC))
                        q.append([newR, newC])
                res += 1
                            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()
                  
        # time complexity: O(n ^ 2)
        # space complexity: O(n ^ 2)
