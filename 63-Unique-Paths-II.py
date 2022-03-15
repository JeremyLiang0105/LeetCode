class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cols = len(obstacleGrid[0])
        rows = len(obstacleGrid)
        
        dp = [[0 for j in range(cols)] for i in range(rows)]
        
        # for cols
        for i in range(cols):
            if obstacleGrid[0][i] == 1: break
            dp[0][i] = 1
            
        # for rows
        for j in range(rows):
            if obstacleGrid[j][0] == 1: break
            dp[j][0] = 1
        
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else: 
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[rows - 1][cols - 1]
      # time complexity: O(m*n)
      # space complexity: O(m*n)
