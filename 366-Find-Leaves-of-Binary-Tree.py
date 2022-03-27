"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def findLeaves(self, root):
        res = []
        def dfs(node):
            if not node:
                return -1
            
            l = dfs(node.left)
            r = dfs(node.right)
            d = max(l, r) + 1
            self.helper(d, res, node.val)
            return d
        dfs(root)
        return res
      
    def helper(self, level, res, val):
        if level == len(res):
            res.append([])
        res[level].append(val)
