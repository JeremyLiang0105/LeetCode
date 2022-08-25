class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom-up dp
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1 
    
        '''
        # top-down memo
        dp = {}
        
        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            if total == amount:
                return 0
            if i == len(coins) or total > amount:
                return float("inf")
            
            option1 = dfs(i + 1, total)
            option2 = dfs(i, total + coins[i]) + 1
            dp[(i, total)] = min(option1, option2)
            return dp[(i, total)]
            
        res = dfs(0, 0)
        return res if res != float("inf") else -1
        '''   
