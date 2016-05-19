"""
Binary Search type

Matrix Search


Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the folstarting properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:

Consider the folstarting matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem

"""

# O( log m + log n)
class Solution:

	def search(self, matrix, target, row):
		start = 0
		end = len(matrix[row])

		while start <= end:
			midIndex = (start + end)//2
			midValue = matrix[row][midIndex]

			if midValue == target:
				return 1

			elif midValue > target:
				end = midIndex - 1

			else:
				start = midIndex + 1
		return 0


	def searchRow(self, matrix, target):
		col = 0
		start = 0
		end = len(matrix) - 1

		while start <= end:
			midIndex = (start + end)//2
			midValue = matrix[midIndex][col]

			if midValue <= target and target <= matrix[midIndex][-1]:
				return midIndex

			elif midValue > target:
				end = midIndex - 1

			else:
				start = midIndex + 1
		return -1


	def searchMatrix(self, matrix, target):
		if not matrix or not matrix[0]:
			return 0

		m = len(matrix)
		n = len(matrix[0])

		validRow = self.searchRow(matrix, target)
		if validRow != -1:
			return self.search(matrix, target, validRow)

		return 0



# O( m + n )
class Solution:
	def valid(self, row, col, m, n):
		return row >= 0 and row < m and col >= 0 and col < n

	def searchMatrix(self, matrix, target):
		if not matrix or not matrix[0]:
			return 0

		m = len(matrix)
		n = len(matrix[0])

		row = 0
		col = n - 1

		while self.valid(row, col, m, n):
			value = matrix[row][col]
			print (row, col, value)

			if target == value:
				return 1

			elif target < value:
				col -= 1

			else:
				row += 1

		return 0


# O( log (m + n ))   FAST!
class Solution:
	def searchMatrix(self, matrix, target):
		if not matrix or not matrix[0]:
			return 0

		m = len(matrix)
		n = len(matrix[0])

		start = 0
		end = m * n - 1

		while start <= end:
			# Handles matrix as a single big sorted array to do regular binary search
			mid = (start + end) // 2
			i = mid // n
			j = (mid - i * n)

			print (mid, i, j)

			if matrix[i][j] == target:
				return 1

			elif matrix[i][j] < target:				
				start = mid + 1

			else:
				end = mid - 1
		return 0


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50],
  [52, 53, 70, 100]
]

target = 21
res = Solution().searchMatrix(matrix, target)

print (res)