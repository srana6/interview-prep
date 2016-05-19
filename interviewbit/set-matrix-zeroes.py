"""
Set Matrix ZerosBookmark


Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

Do it in place.

Example

Given array A as
1 0 1
1 1 1 
1 1 1

On returning, the array A should be :

0 0 0
1 0 1
1 0 1
Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity.

"""

class Solution:

	def changeToZeroes(self, grid, i, j, m, n, row_zero, col_zero):
		grid[i][j] = 0

		if j in col_zero:
			col_zero.remove(j)
			for row in range(m):
				if grid[row][j] != 2:
					grid[row][j] = 0

		if i in row_zero:
			row_zero.remove(i)
			for col in range(n):
				if grid[i][col] != 2:
					grid[i][col] = 0

	# @param grid : list of list of integers
	# @return the same list modified
	def setZeroes(self, grid):
		if not grid or not grid[0]: return grid
		row_zero = set()
		col_zero = set()
		
		m = len(grid)
		n = len(grid[0])

		modified = False
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 0:
					row_zero.add(i)
					col_zero.add(j)
					grid[i][j] = 2
					modified = True

		if modified:
			for i in range(m):
				for j in range(n):
					if grid[i][j] == 2:
						self.changeToZeroes(grid, i, j, m, n, row_zero, col_zero)
		
		return grid

A = [
  [0, 0],
  [1, 1]
]

Solution().setZeroes(A)