class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
        res = []
        def dfs(i, target, comb):
            if len(comb) == k and target == n:
                res.append(comb.copy())
                return
            if len(comb) > k or target > n or i > 9:
                return
            comb.append(i)
            dfs(i + 1, target + i, comb)
            comb.pop()
            dfs(i + 1, target, comb)
        dfs(1, 0, [])
        return res
        '''
        
        res = []
        comb = []
        
        def dfs(i, target):
            if len(comb) == k and target == n:
                res.append(comb.copy())
                return
            if len(comb) > k or target > n or i > 9:
                return
            for num in range(i, 10):
                comb.append(num)
                dfs(num + 1, target + num)
                comb.pop()
        dfs(1, 0)
        return res
