class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        lookup = {}
        res = []
        
        def dfs(i):
            if i in lookup:
                return lookup[i]
            lookup[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            lookup[i] = True
            return True
        
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
    
    # time complexity: O(E + V), where E is the number of edges and V is the number of vertices or nodes
    # space complexity: O(n)
