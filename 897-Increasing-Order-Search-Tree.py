# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        dfs(root)
        
        node = cur = TreeNode()
        for val in lst:
            cur.right = TreeNode(val)
            cur = cur.right
        return node.right
