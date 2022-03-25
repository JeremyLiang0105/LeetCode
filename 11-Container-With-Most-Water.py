class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        last = len(height) - 1
        result = 0
        while start < last:
            tmp = min(height[start], height[last])*(last-start)
            result = max(tmp, result)
            if height[start] < height[last]:
                start += 1
            else:
                last -= 1
        return result
            
        # time complexity: O(n)
        
        '''
        result = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(area, res)
        return result
        
        # time complexity: O(n^2)
        '''
