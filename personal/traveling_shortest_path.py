from heapq import *

"""
Given an undirected graph G having positive weights and N vertices.

You start with having a sum of M money. For passing through a vertex i, you must pay S[i] money. 
If you don’t have enough money – you can’t pass through that vertex. Find the shortest path from 
vertex 1 to vertex N, respecting the above conditions; or state that such path doesn’t exist. 
If there exist more than one path having the same length, then output the cheapest one. 
Restrictions: 1<N<=100 ; 0<=M<=100 ; for each i, 0<=S[i]<=100. 

i  ->  money left
j  ->  vertex

If can pass will have X money left
Recursively when I find a new node that I have enough money for, send recurrence to there
from there try to explore other nodes until reach N
Each time recurre over a node with same amount of money left, I could use that and not repeat
Table[money][vertex]

Solution -> Min[N - 1][j]


"""

from heapq import *

def cheapest_shortest_path(graph, S, M):
	MAX = float("inf")
	n = len(graph)

	states = [False] * n
	Min = [[MAX] * (M + 1) for i in range(n)]
	Min[0][M] = 0

	queue = [(0, str(0) + '-' + str(M))]
	
	
	while queue:
		score, state = heappop(queue)
		k, l = [int(i) for i in state.split('-')]

		if not states[k]:
			for p, weight in enumerate(graph[k]):
				if weight != 0:
					left = l - S[p]
					print ("ASD", left)
					if left >= 0 and Min[p][left] > Min[k][l] + weight:
						Min[p][left] = Min[k][l] + weight
						heappush(queue, (Min[p][left],   str(p) + '-' + str(left)))
						states[k] = True

	result = {
		"weight": MAX,
		"left": 0,
	}

	target = n - 1
	for j in reversed(range(M)):
		if Min[target][j] < result["weight"]:
			result["weight"] = Min[target][j]
			result["left"] = j


	for row in Min:
		print (row)

	print (result)

	print (states)


graph = [
	[1, 2, 9, 8],
	[2, 0, 2, 0],
	[9, 2, 0, 1],
	[8, 0, 1, 2]
]
		
S = [1, 2, 3, 4]
M = 20
cheapest_shortest_path(graph, S, M)


