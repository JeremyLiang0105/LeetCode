class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Base case: check if the sum of nums is odd
        # If it is odd, return False
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2 
        
        for i in range(len(nums) - 1, -1, -1):
            nextdp = set()
            for t in dp:
                nextdp.add(t+nums[i])
                nextdp.add(t)
            dp = nextdp
        return True if target in dp else False
        '''
        Top-Down dfs + memo
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = {}
        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            if total == target:
                return True
            if i == len(nums) or total > target:
                return False
            if dfs(i + 1, total + nums[i]):
                dp[(i + 1, total + nums[i])] = True
                return True
            if dfs(i + 1, total):
                dp[(i + 1, total)] = True
                return True
            dp[(i, total)] = False
            return False
        return dfs(0, 0)
        '''
