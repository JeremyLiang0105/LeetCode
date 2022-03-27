class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(dict)

        for (x, y), val in zip(equations, values):
            adj[x][y] = val
            adj[y][x] = 1.0 / val
        '''
        for i in range(len(equations)):
            adj[equations[i][0]][equations[i][1]] = values[i]
            adj[equations[i][1]][equations[i][0]] = 1 / values[i]
        '''
        def dfs(x, y):
            if x not in adj or y not in adj:
                return -1.0
            # direct connection
            if y in adj[x]:
                return adj[x][y]
            
            for nei in adj[x]:
                if nei not in visited:
                    visited.add(nei)
                    temp = dfs(nei, y)
                    if temp == -1:
                        continue
                    else:
                        return temp * adj[x][nei]
            return -1
        
        res = []
        for p, q in queries:
            visited = set()
            res.append(dfs(p, q))
        return res
