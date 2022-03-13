class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diag = [[] for i in range(len(mat) + len(mat[0]) - 1)]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                diag[r + c].append(mat[r][c])
                
        output = []
        
        for i in range(len(diag)):
            if i % 2 != 0:
                for j in range(len(diag[i])):
                    output.append(diag[i][j])
            else:
                for j in range(len(diag[i]) - 1, -1 ,-1):
                    output.append(diag[i][j])
        return output
      # time complexity: O(m * n)
      # space complexity: O(n)
