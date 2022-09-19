class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        l = 0
        lookup = {}
        res = 0
        for r in range(len(s)):
            lookup[s[r]] = 1 + lookup.get(s[r], 0)
            while len(lookup) > 2:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    del lookup[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
