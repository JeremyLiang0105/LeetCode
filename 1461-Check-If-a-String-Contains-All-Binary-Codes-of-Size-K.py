class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        lookup = set()
        
        for i in range(len(s) - k + 1):
            subStr = s[i:i + k]
            lookup.add(subStr)
        
        n = (1 << k)
        
        return len(lookup) == n
        # return len(lookup) == 2 ** k
        
    # time complexity: O(k*n)
    # space complexity: O(n)
