class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        l = [0] * N
        l[0] = nums[0]
        r = [0] * N
        r[N - 1] = nums[N - 1]
        
        # build our prefix and postfix list
        for i in range(1, N):
            l[i] = l[i - 1] * nums[i]
        for i in range(N - 2, -1, -1):    
            r[i] = r[i + 1] * nums[i]
    
        res = []
        # calculate the product of array
        for i in range(N):
            if i == 0:
                res.append(r[1])
            if i == N - 1:
                res.append(l[N - 2])
            if 1 <= i <= N - 2:
                res.append(l[i - 1] * r[i + 1])
        return res
      
      # time complexity: O(n)
      # space complexity: O(n)
