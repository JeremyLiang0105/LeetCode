"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        level = [root]
        nxtLevel = []
        
        while level:
            for node in level:
                if node.left:
                    node.left.next = node.right
                    node.right.next = None
                    if node.next:
                        node.right.next = node.next.left
                    nxtLevel.append(node.left)
                    nxtLevel.append(node.right)
                else:
                    break
            level = nxtLevel
            nxtLevel = []
        return root
