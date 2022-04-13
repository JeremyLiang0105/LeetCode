class Solution:
  
    def validTree(self, n, edges):
        
        visited = set()
        lookup = {i : [] for i in range(0, n)}

        for start, end in edges:
            lookup[start].append(end)
            lookup[end].append(start)
        
        def dfs(start, prev):
            if start in visited:
                return False
            visited.add(start)
            for nei in lookup[start]:
                if nei == prev:
                    continue
                if dfs(nei, start) == False:
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
