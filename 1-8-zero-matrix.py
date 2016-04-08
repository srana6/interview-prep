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

def clear_matrix(matrix, i, j):
	n = len(matrix)

def zero_matrix(matrix):
	zeros = set()
	n = len(matrix)
	for i in range(n):
		for j in range(n):
			if matrix[i][j] == 0:
				matrix[i][j] = None
	
	for i in range(n):
		for j in range(n):
			if matrix[i][j] == None:
				clear_matrix(matrix, i, j)


