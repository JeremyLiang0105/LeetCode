class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
        
        # time complexity: O(n^2) -> nested loop
        # space complexity: O(n) -> create another dp list to store the data
