from collections import deque
class Solution:
    def shortest_distance(self, grid: List[List[int]]) -> int:
        
        def bfs(r, c):
            q = deque()
            q.append([r, c, 0])
            visited = set()
            while q:
                row, col, cnt = q.popleft()
                for dr, dc in directions:
                    newR = row + dr
                    newC = col + dc
                    if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == 0 and (newR, newC) not in visited:
                        visited.add((newR, newC))
                        q.append([newR, newC, cnt + 1])
                        canReach[newR][newC] += 1
                        dist[newR][newC] += (cnt + 1)
                

        canReach = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        dist = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = float("inf")
        totalBuildings = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    totalBuildings += 1
                    bfs(i, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if canReach[i][j] == totalBuildings and dist[i][j] < res:
                    res = dist[i][j]
        return res if res != float("inf") else -1
