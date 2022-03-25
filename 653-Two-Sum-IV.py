# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lookup = []
        def dfs(node):
            if not node:
                return False
            if node.val in lookup:
                return True
            complement = k - node.val
            lookup.append(complement)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
    
    # time complexity: O(n)
    # space complexity: O(n)
