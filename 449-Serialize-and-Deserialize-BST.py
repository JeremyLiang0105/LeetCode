# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        preorder = []
        def dfs(node):
            if not node:
                return None
            preorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(preorder)
        
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return []
        preOrd = [int(x) for x in data.split(",")]
        inOrd = sorted(preOrd)
        
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None
            node = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            node.left = dfs(preorder[1:idx + 1], inorder[:idx])
            node.right = dfs(preorder[idx + 1:], inorder[idx + 1:])
            return node
        return dfs(preOrd, inOrd)
            
        
        
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
