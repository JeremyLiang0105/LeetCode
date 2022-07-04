class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        '''
        def dfs(i, prev, total):
            nonlocal res
            if i == len(arr):
                res = max(res, total)
                return
            
            for j in range(i, len(arr)):
                if prev == float("inf") or arr[j] - prev == difference:
                    dfs(j + 1, arr[j], total + 1)
                else:
                    dfs(j + 1, prev, total)
            return
        
        res = 0
        dfs(0, float("inf"), 0)
        return res
        '''
        '''
        dp =  {}
        def dfs(prev, i):
            if i == len(arr):
                return 0

            if (prev, i) in dp:
                return dp[(prev, i)]

            op1 = 0 
            if prev == float("inf") or arr[i] - prev == difference:
                op1 = 1 + dfs(arr[i], i + 1)
            op2 = dfs(prev, i + 1)
            
            dp[(prev, i)] = max(op1, op2)
            
            return dp[(prev, i)]

        return dfs(float("inf"), 0)
        '''
        dp = {}
        maxLen = 0
    
        for num in arr:
            dp[num] = dp.get(num-difference, 0) + 1
            maxLen = max(dp[num], maxLen)

        return maxLen
