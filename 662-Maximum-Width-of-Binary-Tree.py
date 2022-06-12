# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        level = [(root, 0)]
        nxtLevel = []
        
        while level:
            for node, index in level:
                if node.left:
                    nxtLevel.append((node.left, 2 * index))
                if node.right:
                    nxtLevel.append((node.right, 2 * index + 1))
            res = max(level[-1][1] - level[0][1] + 1, res)
            level = nxtLevel
            nxtLevel = []
        return res
    
    # left node: 2 * index
    # right node: 2 * index + 1
    # width = maxIndex - minIndex + 1
