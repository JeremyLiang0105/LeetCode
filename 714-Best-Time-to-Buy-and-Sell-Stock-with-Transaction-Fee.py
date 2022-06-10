class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}
        
        def dfs(i, buying):
            if i == len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = -prices[i] + dfs(i + 1, not buying)
                skip = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, skip)
            else:
                sell = prices[i] - fee + dfs(i + 1, not buying)
                skip = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, skip)
            return dp[(i, buying)]
        return dfs(0, True)
