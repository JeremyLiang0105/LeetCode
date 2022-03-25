# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, l, r):
            if not node:
                return True
            elif l >= node.val or r <= node.val:
                return False
            else:
                return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)
        return dfs(root, float('-Inf'), float('Inf'))
