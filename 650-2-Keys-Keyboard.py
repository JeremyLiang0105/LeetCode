class Solution:
    def minSteps(self, n: int) -> int:
        cur = 1
        prev = 0
        res = 0
        
        while cur < n:
            if n % cur == 0: 
                prev = cur # copy
                cur += prev # paste
                res += 2
            else:
                cur += prev # paste
                res += 1
        return res
