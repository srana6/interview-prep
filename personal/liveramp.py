from heapq import *

"""
Incomplete

"""

inf = float("inf")

def count_jumps(river, distance):
	if not river or len(river) < distance: return 0
	n = len(river)
	memo = [None] * n
	
	for i in range(n):
		memo[i] = (river[i], i)
		if river[i] == -1:
			memo[i] = (inf, inf)

	heapify(memo)

	

	
river = [-1, 1, 2, 0, 3, 4]
D = 3

count_jumps(river, D)
