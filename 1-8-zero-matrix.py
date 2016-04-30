"""
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0

Analysis:
	The problem relies on looking for 0's and executing the clearing operation
	without knowing where these were, otherwise it would clear up the whole matrix

	Approach is to traverse the matrix and store the position of the 0's.
	From this algorithm, its not required to store i, j. We could store only the
	row.


	Time: O(n x n)
	Space: O(n)

	TODO:
	Run time is horrible if whole matrix is 0
"""

def clear_row(matrix, row, start = 0):
	for j in range(start, len(matrix)):
		matrix[row][j] = 0

def clear_col(matrix, col, start = 0):
	for i in range(start, len(matrix)):
		matrix[i][col] = 0

def clear_matrix(matrix, first_row = False, first_col = False):		
	for i in range(1, len(matrix)):
		if matrix[i][0] == 0:
			clear_row(matrix, i, 1)

		if matrix[0][i] == 0:
			clear_col(matrix, i, 1)

	if first_row: clear_row(matrix, 0)
	if first_col: clear_col(matrix, 0)


def zero_matrix(matrix):	
	n = len(matrix)
	first_col = False
	first_row = False

	for i in range(n):
		if matrix[i][0] == 0:
			first_col = True

		if matrix[0][i] == 0:
			first_row = True

	for i in range(n):
		for j in range(n):
			if matrix[i][j] == 0:
				matrix[i][0] = 0
				matrix[0][j] = 0

	clear_matrix(matrix, first_row, first_col)

matrix = [
	[1, 0, 3, 4],
	[2, 3, 7, 8],
	[6, 4, 0, 1],
	[8, 3, 5, 2]
]

zero_matrix(matrix)

for i in range(len(matrix)):
	print (matrix[i])