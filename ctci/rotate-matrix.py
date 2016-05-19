"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate(matrix):
	N = len(matrix)

	for layer in range(int(N / 2)):		
		outlayer = N - layer - 1
		for j in range(layer, outlayer):
			aux = matrix[layer][j]
			matrix[layer][j] = matrix[outlayer - j][layer]
			matrix[outlayer - j][layer] = matrix[outlayer][outlayer - j]
			matrix[outlayer][outlayer - j] = matrix[j][outlayer]
			matrix[j][outlayer] = aux

matrix = [
	[1,  2,  3,  4,   5],
	[6,  7,  8,  9,  10],
	[11, 12, 13, 14, 15],
	[16, 17, 18, 19, 20],
	[21, 21, 22, 23, 24]
]

rotate(matrix)

for row in matrix:
	print (row)