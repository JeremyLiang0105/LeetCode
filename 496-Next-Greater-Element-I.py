class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        lookup = {}
        res = []
        for i in range(len(nums2)):
            lookup[nums2[i]] = i
        
        for n in nums1:
            index = lookup[n]
            flag = True
            for i in range(index + 1, len(nums2)):
                if nums2[i] > n:
                    res.append(nums2[i])
                    flag = False
                    break
            if flag == True:
                res.append(-1)
        return res
        
        # time complexity: O(m * n)
        '''
        
        lookup = {}
        for i in range(len(nums1)):
            lookup[nums1[i]] = i
        res = [-1] * len(nums1)
        stack = []
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                index = lookup[val]
                res[index] = cur
            if cur in lookup:
                stack.append(cur)
        return res
    
    # time complexity: O(m + n)
    # space complexity: O(n)
