class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        
        def dfs(i, total):
            if total == target:
                res.append(comb.copy())
                return
            if i >= len(candidates) or total > target:
                return
            comb.append(candidates[i])
            dfs(i, total + candidates[i])
            comb.pop()
            dfs(i + 1, total)
        dfs(0, 0)
        return res
    
        # time complexity: O(2^t) where t is the target value
        # space complexity: O(n)
