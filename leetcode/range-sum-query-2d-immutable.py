class NumMatrix(object):

    def __init__(self, matrix):
        if matrix is None or not matrix:
            return        
        r, c = len(matrix), len(matrix[0])
        self.sums = [[0 for j in range(c + 1)] for i in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):            
                self.sums[i][j] = matrix[i-1][j-1] + self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.sums[row2][col2] - self.sums[row2][col1-1] - self.sums[row1-1][col2] + self.sums[row1-1][col1-1]


class NumMatrix_slow(object):

    def __init__(self, matrix):
        if matrix is None or not matrix:
            return
        self.matrix = matrix
        self.r, self.c = len(matrix), len(matrix[0])

        diag = 0
        left = 0
        up = 0


        self.sums = [[0 for j in range(self.c)] for i in range(self.r)]

        for i in range(self.r):
            for j in range(self.c):
                diag = NumMatrix.matrix_pos(self.r, self.c, i - 1, j - 1, self.sums)
                left = NumMatrix.matrix_pos(self.r, self.c, i, j - 1, self.sums)
                up =   NumMatrix.matrix_pos(self.r, self.c, i - 1, j, self.sums)                
                self.sums[i][j] = matrix[i][j] + left + up - diag

    @staticmethod
    def matrix_pos(rows, columns, i, j, matrix):
        if  ( i >= 0 and i < rows ) and ( j >= 0 and j < columns ):
            return matrix[i][j] 
        return 0

    def sumRegion(self, row1, col1, row2, col2):
        diag = NumMatrix.matrix_pos(self.r, self.c, row1 - 1, col1 - 1, self.sums)
        left = NumMatrix.matrix_pos(self.r, self.c, row2, col1 - 1, self.sums)
        up =   NumMatrix.matrix_pos(self.r, self.c, row1 - 1, col2, self.sums)

        return self.sums[row2][col2] - left - up + diag
        







        
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

numMatrix = NumMatrix(matrix)


# Your NumMatrix object will be instantiated and called as such:
print (numMatrix.sumRegion(2, 1, 4, 3))
print (numMatrix.sumRegion(1, 1, 2, 2))
print (numMatrix.sumRegion(1, 2, 2, 4))






matrix = [[-4,-5]]
numMatrix = NumMatrix(matrix)


# Your NumMatrix object will be instantiated and called as such:
print (numMatrix.sumRegion(0,0,0,0))
print (numMatrix.sumRegion(0,0,0,1))
print (numMatrix.sumRegion(0,1,0,1))

