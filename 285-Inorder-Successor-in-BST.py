"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    def inorderSuccessor(self, root, p):
        # inorder: LCR
        cur = root
        prev = None
        while cur != None:
            if cur.val > p.val:
                prev = cur
                cur = cur.left
            else:
                cur = cur.right
        return prev
    
    # time complexity: O(n) where n is the number of nodes in the tree
    # space complexity: O(1)
