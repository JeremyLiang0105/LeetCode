# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        lookup = {}
        res = []
        
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            v = l + r + node.val
            
            lookup[v] = 1 + lookup.get(v, 0)
            return v
        dfs(root)
        
        max_val = max(lookup.values())
        for val, cnt in lookup.items():
            if cnt == max_val:
                res.append(val)
        return res
