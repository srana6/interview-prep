class Solution(object):	
	def spiralOrder(self, matrix):
		if not matrix or not matrix[0]: 
			return []
		
		n = len(matrix)
		m = len(matrix[0])
		total = n * m
		spiral = []

		iMin = 0
		iMax = n

		jMin = 0
		jMax = m
		
		i = 0
		j = 0

		while iMin <= iMax and jMin <= jMax:


			while j <=  jMax: 
				spiral.append(matrix[i][j])
				j += 1
				if j + jMin == jMax: 
					j -= 1
					i += 1
					break


			while i <=  iMax: 
				spiral.append(matrix[i][j])
				i +=1
				if i + iMin == iMax: 
					i -= 1
					j -= 1
					break
			

			while j >= jMin: 
				spiral.append(matrix[i][j])
				j -= 1				
				if j + jMin == jMin: 
					
					j += 1
					break
					
			print ("YAY", i, iMin, j)

			while i >= iMin: 
				spiral.append(matrix[i][j])
				i -= 1
				if i < iMin: 
					i += 1
					break

			iMin +=1
			jMax +=1

		return order
		
		

def performOps(A):
	m = len(A)
	n = len(A[0])
	B = []
	for i in range(len(A)):
		B.append([0] * n)
		for j in range(len(A[i])):
			B[i][n - 1 - j] = A[i][j]
	return B


A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
B = performOps(A)
for i in range(len(B)):
	for j in range(len(B[i])):
		print (B[i][j])


grid = [
	[ 1, 2, 3 ],
	[ 4, 5, 6 ],
	[ 7, 8, 9 ]
]


Solution().spiralOrder(grid)