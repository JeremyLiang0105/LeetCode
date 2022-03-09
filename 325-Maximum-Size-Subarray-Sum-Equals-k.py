class Solution:
    def max_sub_array_len(self, nums: List[int], k: int) -> int:
        lookup = {0 : -1}
        curS = 0
        res = 0
        for index, num in enumerate(nums):
            curS += num
            diff = curS - k
            if diff in lookup:
                res = max(res, index - lookup[diff])
            if curS not in lookup:
                lookup[curS] = index
        return res
      
    # time complexity: O(n)
    # space complexity: O(n)
