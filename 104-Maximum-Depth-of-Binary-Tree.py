# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = 0
        queue = [root]
        level = []
        
        while queue != [] and root is not None:
            res += 1
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
            level = []
        return res
        
        '''
        def dfs(node):
            if not node:
                return 0
            else:
                return max(dfs(node.left), dfs(node.right)) + 1
        return dfs(root)
        
        # time complexity: O(n)
        # space complexity : height of the tree, worst case O(n)
        #if root is None:
        #    return 0
        #return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        '''
