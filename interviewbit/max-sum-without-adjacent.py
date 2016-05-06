"""
Given a 2 * N Grid of numbers, choose numbers such that the sum of the numbers
is maximum and no two chosen numbers are adjacent horizontally, vertically or 
diagonally, and return it.

Example:

Grid:
	1 2 3 4
	2 3 4 5

	2 3 4 5

so we will choose
3 and 5 so sum will be 3 + 5 = 8

Note that you can choose more than 2 numbers
"""

class Solution:
	# @param A : list of list of integers
	# @return an integer

	def adjacent(self, grid):
		if not grid and not grid[0]: return 0
		if len(grid[0]) == 1: return max(grid[0][0], grid[1][0])

		m = len(grid)
		n = len(grid[0])
		last = n - 1

		memo = [0] * n
		memo[0] = max(grid[0][0], grid[1][0])
		memo[1] = max(grid[0][1], grid[1][1], memo[0])

		for i in range(2, n):
			temp = max(grid[0][i], grid[1][i])
			memo[i] = max(memo[i - 1], temp, memo[i - 2] + temp)			
			
		return memo[last]

grid = [
	[2, 68],
	[13, 4]
]
		
Solution().adjacent(grid)


