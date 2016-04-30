"""
135. - 8.2
Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are 'off limits'
such that the robot cannot step on them.
Design an algorithm to find a path for the robot from the top left to the bottom right
"""
# O(rc)

import unittest

def robot_path(grid):
	if not grid or not grid[0]:
		return None

	r = len(grid)
	c = len(grid[0])

	memo = [[None for x in range(c)] for y in range(r)]
	memo[0][0] = (0, 0)

	for i in range(r):
		for j in range(c):
			if grid[i][j]:					
				if j - 1 >= 0 and grid[i][j - 1]:
					memo[i][j] = (i, j - 1)

				if i - 1 >= 0 and grid[i - 1][j]:
					memo[i][j] = (i - 1, j)		

	if memo[r-1][c-1] is not None:
		r = r - 1
		c = c - 1
		path = []
		while (r, c) != (0, 0):
			path.append((r, c))
			r, c = memo[r][c]
		path.append((0, 0))

		return path[::-1]

	return None



class Test(unittest.TestCase):
	data = [
		([[1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0], [1, 1, 1, 1]], [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (4, 2), (4, 3)]),
		([[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 0, 1]], [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)])
	]

	def test_path(self):
		for (grid, expected) in self.data:
			self.assertEqual(robot_path(grid), expected)

unittest.main()