# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        
        def dfs(node):
            nonlocal res
            if not node:
                return None 
            l = dfs(node.left)
            r = dfs(node.right)
            tmp = ""
            if l or r:
                if l:
                    tmp += ("(" + str(l) + ")")
                else:
                    tmp += "()"
                if r:
                    tmp += ("(" + str(r) + ")")
            res = str(node.val) + tmp
            return res
        return dfs(root)
