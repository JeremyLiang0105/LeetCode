class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''
        l = 0
        res = 0
        
        while l < len(nums):
            total = 0
            for r in range(l, len(nums)):
                total += nums[r]
                if total % k == 0:
                    res += 1
            l += 1
        return res
        '''
        
        lookup = {0 : 1}
        curSum = 0
        res = 0
        
        for num in nums:
            curSum += num
            remainder = curSum % k
            res += lookup.get(remainder, 0)
            lookup[remainder] = 1 + lookup.get(remainder, 0)
        return res
