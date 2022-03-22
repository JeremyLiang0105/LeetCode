class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        lookup = collections.defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                lookup[i].append(graph[i][j])
    
        tmp = [0]
        res = []
      
        def dfs(i):
            if i == len(graph) - 1:
                res.append(tmp.copy())
                return
            for nei in lookup[i]:
                tmp.append(nei)
                dfs(nei)
                tmp.pop()
        dfs(0)
        return res
