"""

Min Steps in Infinite GridBookmark

You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
	(x+1, y), 
	(x - 1, y), 
	(x, y+1), 
	(x, y-1), 
	(x-1, y-1), 
	(x+1,y+1), 
	(x-1,y+1), 
	(x+1,y-1) 

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

This question is intentionally left slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.

"""

import math

class Solution:

	moves = 8
	movesX = [-1, 0,  1, 1, 1, 0, -1, -1]
	movesY = [-1, -1,-1, 0, 1, 1,  1,  0]

	def eucledian_distance(self, x1, y1, x2, y2):
		return math.sqrt( pow(x1 - x2, 2) + pow(y1 - y2, 2) )

	# @param X : list of integers
	# @param Y : list of integers
	# Points are represented by (X[i], Y[i])
	# @return an integer
	def coverPoints(self, X, Y):
		if not X or not Y or len(X) != len(Y): return 0
		n = len(X)
		totalMoves = 0
		minIndex = 0
		minDist = 0

		curX, curY = X[0], Y[0]		
		i = 1
		while i < n:
			if self.eucledian_distance(curX, curY, X[i], Y[i]) == 0.0:
				i += 1

			else:
				minIndex = -1
				minDist = float("inf")

				for m in range(self.moves):
					distance = self.eucledian_distance(curX + self.movesX[m], curY + self.movesY[m], X[i], Y[i])
					if distance < minDist:
						minDist = distance
						minIndex = m

				curX += self.movesX[minIndex]
				curY += self.movesY[minIndex]
				totalMoves += 1

		return totalMoves

	

	
	def coverPoints(self, X, Y):
		if not X or not Y or len(X) != len(Y) or len(X) == 1: return 0
		n = len(X)
		answer = 0

		for i in range(1, n):
			answer += max( abs(X[i] - X[i - 1]),  abs(Y[i] - Y[i - 1]) )

		return answer


A = [ -4, 1, -4, 8, -11, -12, -13, -3, -4, -4, -14, 7, -2, -2, -5, 5, -1, 0 ]
B = [ -8, -15, -4, 3, 11, 8, -15, 4, 1, 7, 3, 9, -9, -9, -13, 10, -14, -8 ]

sol = Solution().coverPoints(A, B)

print (sol)