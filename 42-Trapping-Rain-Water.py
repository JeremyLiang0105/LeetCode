class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        res = 0
        
        maxLeft = [0 for i in range(len(height))]
        for i in range(1, len(height)):
            l = max(height[:i])
            maxLeft[i] = l
            
        maxRight = [0 for i in range(len(height))]
        for i in range(len(height) - 2, -1, -1):
            r = max(height[i + 1:])
            maxRight[i] = r
            
        # maxRight.reverse()
        lookup = [0 for i in range(len(height))]
        for i in range(len(maxLeft)):
            tmp = min(maxLeft[i], maxRight[i])
            lookup[i] = tmp
            
        for i in range(len(height)):
            water = (lookup[i] - height[i])
            if water > 0:
                res += water
        return res
    
    # time complexity: O(n)
    # space complexity: O(n)
