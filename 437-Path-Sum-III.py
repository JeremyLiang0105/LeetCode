# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    def help(self, root, total_sum):
        if root == None:
            return 0
        cur = (root.val == total_sum)
        cur += self.help(root.left, total_sum - root.val)
        cur += self.help(root.right, total_sum - root.val)
        return cur
        
        if not root:
            return 0
        if root.val == total_sum:
            cur = 1
        else:
            cur = 0
        cur += self.help(root.left, total_sum - root.val)
        cur += self.help(root.right, total_sum - root.val)
        return cur
    
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root == None:
            return 0
        return self.help(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    
    # time complexity: O(n^2)
    # space complexity: O(1)
    '''
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        lookup = {0 : 1}
        
        return self.helper(root, 0, targetSum, lookup)
    
    def helper(self, node, curr, target, lookup):
        if not node:
            return 0
        
        curr += node.val
        temp = curr - target
        count = lookup.get(temp, 0)
        lookup[curr] = 1 + lookup.get(curr, 0)
        count += self.helper(node.left, curr, target, lookup) + self.helper(node.right, curr, target, lookup)
        lookup[curr] = lookup.get(curr) - 1
        return count
    # time complexity: O(n)
    # space complexity: O(n)
