class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [0] * 3
        col = [0] * 3
        posDiag = 0
        negDiag = 0
        player = 1
        
        for x, y in moves:
            row[x] += player
            col[y] += player
            if x == y:
                posDiag += player
            if x + y == 2:
                negDiag += player
            if abs(row[x]) == 3 or abs(col[y]) == 3 or abs(posDiag) == 3 or abs(negDiag) == 3:
                if player == 1:
                    return "A"
                else:
                    return "B"
            player *= -1
        
        if len(moves) == 3 * 3:
            return "Draw"
        else:
            return "Pending"
        
