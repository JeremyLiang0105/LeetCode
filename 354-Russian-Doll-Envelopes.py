class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        dp = [1] * len(envelopes)
        maxNum = 1
        
        for i in range(1, len(envelopes)):
            for j in range(0, i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxNum = max(maxNum, dp[i])
        return maxNum
