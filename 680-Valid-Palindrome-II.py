class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(s):
            return s == s[::-1]
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPal(s[l:r]) or isPal(s[l + 1: r + 1])
        return True
