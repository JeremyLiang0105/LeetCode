class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                # hours += pile // k
                # hours += 1 if pile % k != 0 else 0
                hours += math.ceil(pile / k) # round up
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
    
    # time complexity: O(log(max(piles)) * len(piles))
