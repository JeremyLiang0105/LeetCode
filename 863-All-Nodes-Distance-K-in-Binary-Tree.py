# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, lookup, node, parent):
        if parent:
            lookup[node].append(parent)
        if node.left:
            lookup[node].append(node.left)
            self.dfs(lookup, node.left, node)
        if node.right:
            lookup[node].append(node.right)
            self.dfs(lookup, node.right, node)
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        lookup = collections.defaultdict(list)
        self.dfs(lookup, root, None)
        
        q = deque([(target, 0)])
        res = []
        visited = {target}
        while q:
            node, dist = q.popleft()
            if dist > k:
                break
            if k == dist:
                res.append(node.val)
            for nei in lookup[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, dist + 1))
        return res
