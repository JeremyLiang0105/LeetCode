class Solution:
    def minJumps(self, arr: List[int]) -> int:
        '''
        visited = set()
        res = float("inf")
        
        def dfs(i, cnt):
            nonlocal res
            if i < 0 or i >= len(arr) or i in visited:
                return 
            if i == len(arr) - 1:
                res = min(res, cnt)
                return
            
            visited.add(i)
            dfs(i + 1, cnt + 1)
            dfs(i - 1, cnt + 1)
            
            for j in range(len(arr)):
                if j > i and arr[j] == arr[i]:
                    dfs(j, cnt + 1)
            visited.remove(i)
        
        dfs(0, 0)
        return res
        '''
        '''
        q = deque([(0, 0)])
        visited = set()
        visited.add(0)
        
        while q:
            i, step = q.popleft()
            if i == len(arr) - 1:
                return step
            for j in range(len(arr)):
                if j == i - 1 or j == i + 1 or arr[i] == arr[j]:
                    if j not in visited:
                        visited.add(j)
                        q.append([j, step + 1])
        '''
        q = deque([(0, 0)])
        visited = set()
        visited.add(0)
        lookup = collections.defaultdict(list)
        for i, v in enumerate(arr):
            lookup[v].append(i)
            
        while q:
            i, step = q.popleft()
            if i == len(arr) - 1:
                return step
            for j in [*lookup[arr[i]], i + 1, i - 1]:
                    if 0 <= j < len(arr) and j not in visited:
                        visited.add(j)
                        q.append([j, step + 1])
            lookup[arr[i]].clear()
