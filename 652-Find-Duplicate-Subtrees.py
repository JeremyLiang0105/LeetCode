# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        lookup = {}
        
        def dfs(node):
            if not node:
                return "N"
            l = dfs(node.left)
            r = dfs(node.right)
            path = str(node.val) + "," + l + "," + r
            lookup[path] = 1 + lookup.get(path, 0)
            if lookup[path] == 2:
                res.append(node)
            return path
        dfs(root)
        return res
    
    # time complexity: O(n^2)
