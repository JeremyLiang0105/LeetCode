class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp = [[0 for col in range(m)] for row in range(n)]
        dp = [[0 for j in range(m)] for i in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for j in range(n):
            dp[j][0] = 1
        
        for row in range(1, n):
            for col in range(1, m):
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
        return dp[n-1][m - 1]
    
    # time complexity: O(m*n)
    # space complexity: O(m*n)
