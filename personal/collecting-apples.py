"""

Problem:
A table composed of N x M cells, each having a certain quantity of apples, is given. 
You start from the upper-left corner. At each step you can go down or right one cell.
Find the maximum number of apples you can collect.

Brute Force:
	Recursively, go down or left, and explore all cells
	Time complexity becomes exponential

Analysis:
	Store the max amount of apples for each cell, use this sub-problem to go 
	the other side

	Recurrence would be such as:
	A[i][j] =  max( up,  left)



"""

def get_apple(apples, i, j, n, m):
	if i >= 0 and i < n and j >= 0 and j < m:
		return apples[i][j]
	else: 
		return 0

def collect_max_apples(apples):
	if not apples: return

	n = len(apples)
	m = len(apples[0])
	table = [[0] * m for i in range(n)]

	for i in range(n):
		for j in range(m):
			table[i][j] = apples[i][j] + max(get_apple(table, i - 1, j, n, m), 
											 get_apple(table, i, j - 1, n, m))

	for row in table:
		print (row)

	return table[n - 1][m - 1]


apples = [
	[2, 5, 1, 0],
	[1, 9, 1, 0],
	[0, 0, 1, 0],
	[8, 2, 0, 1]
]

collect_max_apples(apples)