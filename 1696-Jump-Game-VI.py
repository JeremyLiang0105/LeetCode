class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        '''
        dp = [float("-inf")] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            for j in range(1, k + 1):
                if i - j >= 0:
                    dp[i] = max(dp[i], nums[i] + dp[i - j])  
        return dp[-1]
        '''
        maxHeap = [(-nums[0], 0)]
        
        for i in range(1, len(nums)):
            while maxHeap[0][1] < i - k:
                heapq.heappop(maxHeap)
            m = maxHeap[0][0]
            heapq.heappush(maxHeap, (m - nums[i], i))
            if i == len(nums) - 1:
                return -(m - nums[i])
        return nums[0]
    
    # time complexity: O(nlogn)
    # space complexity: O(n)
    
