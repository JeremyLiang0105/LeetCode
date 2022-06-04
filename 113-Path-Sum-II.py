# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    def helper(self, root, tot_sum, lst, res):
        if root.left == None and root.right == None:
            if root.val == tot_sum:
                res += [lst + [root.val]]
        if root.left:
            self.helper(root.left, tot_sum - root.val, lst + [root.val], res)
        if root.right:
            self.helper(root.right, tot_sum - root.val, lst + [root.val], res)
        return res
     '''   
        
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        if root == None:
            return res
        
        def helper(root, tot_sum, lst):
            if root == None:
                return None
            if root.left == None and root.right == None:
                if root.val == tot_sum:
                    res.append(lst + [root.val])
                    return
            
            helper(root.left, tot_sum - root.val, lst + [root.val])
            helper(root.right, tot_sum - root.val, lst + [root.val])
        helper(root, targetSum, [])
        return res
    
    # time complexity: O(n) where n is the number of nodes
    # space complexity: O(h) where h is the height of the tree
