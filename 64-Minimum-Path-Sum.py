class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        rows = len(grid)
        cols = len(grid[0])
        
        for j in range(1, cols):
            grid[0][j] += grid[0][j-1]
        for i in range(1, rows):
            grid[i][0] += grid[i-1][0]
        
        for row in range(1, rows):
            for col in range(1, cols):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        
        return grid[rows-1][cols-1]
        '''
        m = len(grid)
        n = len(grid[0])
        dp = {}
        
        def helper(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= m or j >= n:
                return float('inf')
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            res = grid[i][j] + min(helper(i + 1, j), helper(i, j + 1))
            dp[(i, j)] = res
            return res
        
        return helper(0, 0)
        '''
        m = len(grid)
        n = len(grid[0])
                
        def helper(i,j):
            if i >= m or j>=n:
                return float('inf')
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            return grid[i][j] + min(helper(i + 1,j), helper(i,j + 1))
            
        
        return helper(0,0)
        '''
