class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        visited = set()
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 
            
            for n in nums:
                if n in visited:
                    continue
                visited.add(n)
                perm.append(n)
                dfs()
                perm.pop()
                visited.remove(n)
                
        dfs()
        return res
