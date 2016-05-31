"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees, Can you do this in place?

Analysis
	We can rotate values by level, or layer.
	Iterating by the number of elements on each layer and swaping continuously.

	Due to touching each position once, the run time is the size of the matrix
	Time: O(NxN)
	Space: O(1)
"""

def rotate_matrix(matrix):
	n = len(matrix)
	layers = n // 2

	for layer in range(layers):
		first = layer
		last = n - layer - 1
		for i in range(first, last):
			offset = i - first
			temp = matrix[first][i]

			matrix[first][i] = matrix[last - offset][first]
			matrix[last - offset][first] = matrix[last][last - offset]
			matrix[last][last - offset] = matrix[i][last]
			matrix[i][last] = temp

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]
]

rotate_matrix(matrix)

for i in range(len(matrix)):
	print (matrix[i])