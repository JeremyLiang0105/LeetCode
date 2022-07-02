"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        if not root:
            return 0
        self.length = 1
        self.search(root)
        return self.length
    
    def search(self, root):
        if not root:
            return [0, 0]
        up_length = 1
        down_length = 1
        left = self.search(root.left)
        right = self.search(root.right)
        if root.left:
            if root.left.val - 1 == root.val: 
                up_length = max(up_length, left[0] + 1)
            if root.left.val + 1 == root.val:
                down_length = max(down_length, left[1] + 1)
        if root.right:
            if root.right.val - 1 == root.val:
                up_length = max(up_length, right[0] + 1)
            if root.right.val + 1 == root.val:
                down_length = max(down_length, right[1] + 1)
        self.length = max(self.length, up_length + down_length - 1)
        return [up_length, down_length]
