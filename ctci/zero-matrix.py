"""
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0
"""


def setZero(matrix, M, N, rows, cols):
	for row in rows:		
		for x in range(N):
			matrix[row][x] = 0

	for col in cols:
		for y in range(M):
			matrix[y][col] = 0

def zeroMatrix(matrix):
	rows = {}
	cols = {}

	M, N = len(matrix), len(matrix[0])	
	for i in range(M):
		for j in range(N):
			if j not in cols:				
				if matrix[i][j] == 0:
					rows[i] = True
					cols[j] = True
					break

	setZero(matrix, M, N, rows, cols)

matrix = [
	[0,  2,  3,  4,   5],
	[6,  0,  8,  9,  10],
	[11, 12, 0, 14, 15],
	[16, 17, 0, 19, 20],
	[21, 21, 22, 23, 24],
	[25, 26, 27, 28, 29]
]


zeroMatrix(matrix)


for row in matrix:
	print (row)