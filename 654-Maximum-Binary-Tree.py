# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
      
        def dfs(nums):
            if not nums:
                return None
            index = 0
            val = 0
            for i, v in enumerate(nums):
                if v > val:
                    val = v
                    index = i
            node = TreeNode(val)
            node.left = dfs(nums[:index])
            node.right = dfs(nums[index + 1:])
            return node
          
        return dfs(nums)
    '''
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        max_val = max(nums)
        index = nums.index(max_val)
        
        node = TreeNode(max_val)
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index+1:])
        
        return node
    '''
