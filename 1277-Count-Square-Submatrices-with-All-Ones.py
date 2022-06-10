class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = {}
        
        # dfs + memo
        
        def dfs(r, c):
            if r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] == 0:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            dp[(r, c)] = 0
            down = dfs(r + 1, c)
            right = dfs(r, c + 1)
            diag = dfs(r + 1, c + 1)
            if matrix[r][c] == 1:
                dp[(r, c)] = 1 + min(down, right, diag)
            return dp[(r, c)]
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res += dfs(i, j)
        return res
