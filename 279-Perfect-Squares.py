class Solution:
    def numSquares(self, n: int) -> int:
        '''
        dp = [n] * (n + 1)
        dp[0] = 0
        
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if square > target:
                    break
                dp[target] = min(dp[target], dp[target - square] + 1)
        return dp[n]
        '''
        dp = {}
        def dfs(total):
            if total in dp:
                return dp[total]
            if total == n:
                return 0
            if total > n:
                return float("inf")
            res = float("inf")
            for i in range(1, int(sqrt(n)) + 1):
                res = min(res, 1 + dfs(total + i * i))
            dp[total] = res
            return res
        return dfs(0)
    # time complexity: O(n * sqrt(n))
