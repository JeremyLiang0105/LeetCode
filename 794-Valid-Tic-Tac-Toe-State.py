class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        X = 0
        O = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    X += 1
                if board[i][j] == "O":
                    O += 1
        
        if O > X or X - O > 1:
            return False
        if X == O and self.win(board, "X"):
            return False
        if X == O + 1 and self.win(board, "O"):
            return False
        return True
        
    def win(self, board, char):
        for i in range(len(board)):
            if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] == char:
                return True
        for j in range(len(board)):
            if board[0][j] == board[1][j] and board[0][j] == board[2][j] and board[0][j] == char:
                return True
        if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == char:
            return True
        if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == char:
            return True
