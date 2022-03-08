class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft() 
                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc
                    if (newR < 0 or newC < 0 or newR == len(grid) or newC == len(grid[0]) or grid[newR][newC] != 1):
                        continue
                    grid[newR][newC] = 2
                    q.append([newR, newC])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
        
        # time complexity: O(m * n)
        # space complexity: O(m * n)
