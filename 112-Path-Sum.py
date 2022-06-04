# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False
            curSum += node.val
            if node.left == None and node.right == None:
                return curSum == targetSum
            return dfs(node.left, curSum) or dfs(node.right, curSum)
        return dfs(root, 0)
   
    # time complexity: O(n) where n is the number of nodes
    # space compexity: O(h) -> O(logn) where h is the height of the tree
