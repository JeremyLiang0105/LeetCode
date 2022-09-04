class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        lookup = {}
        maxFreq = 0
        
        for r in range(len(s)):
            lookup[s[r]] = 1 + lookup.get(s[r], 0)
            maxFreq = max(maxFreq, lookup[s[r]])
            while (r - l + 1) - maxFreq  > k:
                lookup[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
    
    # sliding window
    # time complexity: O(n)
    # space complexity: O(1)
