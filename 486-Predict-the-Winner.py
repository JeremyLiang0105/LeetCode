class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i > j:
                return 0
            sum1 = nums[i] + min(dfs(i + 2, j), dfs(i + 1, j - 1))
            sum2 = nums[j] + min(dfs(i + 1, j - 1), dfs(i, j - 2))
            score = max(sum1, sum2)
            dp[(i, j)] = score
            return score
        
        p1 = dfs(0, len(nums) - 1)
        return p1 >= sum(nums) - p1
