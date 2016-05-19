from collections import deque

class Graph:
	def __init__(self, graph):
		self.graph = graph
	
	def route_between(self, start, end, path=[]):
		if start == end:
			return True

		visited = set([start])
		queue = deque(start)
		found = False

		while queue and not found:
			u = queue.popleft()
			for v in self.graph[u]:
				if v not in visited:
					if v == end:
						found = True
						break
					else:
						visited.add(v)
						queue.append(v)
		return found




graph = {
	'A': ['B', 'C'],         
	'B': ['A', 'D', 'E'],
	'C': ['A', 'F'],
	'D': ['B'],
	'E': ['B', 'F'],
	'F': ['C', 'E']
}

sol = Graph(graph)
print (sol.route_between('A', 'E'))
