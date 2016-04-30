"""
Imagine a robot sitting on the upper left corner of  grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are 
'off limits' such that the robot cannot step on them.

Design an algorithm to find a path for the robot from the top left to the bottom
right.


Analysis: 
	Note:  Grid can be a Boolean Matrix, where False means a step is not possible.

	Brute Force:
		For each of the paths, recur over each of the cells, either right or left.
		For all possible paths, store the minimum and return that
		O( 2^(n^2) )

	Solution 1:
		Maintance a distance matrix to store the optimum solution until each cell	
		O( n^2 )
"""

def valid_move(i, j):
	return i >= 0 and j >= 0


def find_robot_path(grid):
	if not grid: return None

	MAX = float("inf")
	N = len(grid)
	distance = [[MAX] * N  for i in range(N)]
	distance[0][0] = 0

	path = []

	for r in range(N):
		for c in range(N):
			if grid[r][c]:
				if valid_move(r - 1, c):
					distance[r][c] = min(distance[r][c], 1 + distance[r - 1][c])

				if valid_move(r, c - 1):
					distance[r][c] = min(distance[r][c], 1 + distance[r][c - 1])

	for row in distance:
		print (row)




def _getPath(grid, row, col, path, cache):
	if row < 0 or col < 0 or not grid[row][col]:
		return False

	if (row, col) in cache:
		return cache[(row, col)]

	origin = (row == 0 and col == 0)
	success = False
	if origin or _getPath(grid, row, col - 1, path, cache) or _getPath(grid, row - 1, col, path, cache):
		path.append((row, col))
		success = True

	cache[(row, col)] = success
	return success

def getPath(grid):
	if not grid: return None
	path = []
	cache = {}
	lastRow = len(grid) - 1
	lastCol = len(grid[0]) - 1

	if _getPath(grid, lastRow, lastCol, path, cache):
		return path
	return None



grid = [
	[True, True, True, True],
	[True, False, True, True],
	[True, True, False, False],
	[True, True, True, True]	
]


find_robot_path(grid)
solution = getPath(grid)

print (solution)