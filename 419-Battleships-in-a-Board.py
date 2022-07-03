class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in visited or board[r][c] == ".":
                return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        res = 0
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X" and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        return res
