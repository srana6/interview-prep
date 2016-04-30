from heapq import *

"""

This is a Dijkstra

"""

def shortest_path(graph, node_from, node_to):
	MAX = float("inf")
	n = len(graph)

	visited = set()
	parent = [None] * n
	distance = [MAX] * n
	distance[node_from] = 0
	
	queue = [(0, node_from)]

	while queue:
		score, u = heappop(queue)
		visited.add(u)

		for v, weight in enumerate(graph[u]):
			if weight != 0 and v not in visited:
				if distance[v] > distance[u] + weight:
					distance[v] = distance[u] + weight
					parent[v] = u
					heappush(queue, (distance[v], v)) 

	print (distance)


G = [
	[0,  6,  9,  0],
	[0,  0,  0,  1],
	[0, -5,  0,  2],
	[0,  0,  0,  0]
]

shortest_path(G, 0, 3)