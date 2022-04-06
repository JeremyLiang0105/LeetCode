# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        lookup = collections.defaultdict(list)
        level = [(0, 0, root)]
        nxtLevel = []
        
        while level:
            for n in level:
                row, col, node = n
                lookup[col].append((row, node.val))
                if node.left:
                    nxtLevel.append((row + 1, col - 1, node.left))
                if node.right:
                    nxtLevel.append((row + 1, col + 1, node.right))
            level = nxtLevel
            nxtLevel = []
            
        res = []
        for key in sorted(lookup.keys()):
            # sort first by row, then value of the node
            res.append([val for row, val in sorted(lookup[key])])
        return res
