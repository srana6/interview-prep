from collections import deque
MAX = float("inf")

class Solution(object):
	def getHeight(self, n, start, edges):
		height = 0
		visited = set()
		queue = deque([start])
		distance = [MAX] * n
		distance[start] = 0
		
		while queue:
			u = queue.pop()
			visited.add(u)
			
			for edge in edges:
				v = None
				if u == edge[0]:
					v = edge[1]
				elif u == edge[1]:
					v = edge[0]
				
				if v is not None:
					if v not in visited:
						queue.appendleft(v)
						distance[v] = distance[u] + 1
						height = max(height, distance[v])
		return height
	
	def findMinHeightTrees(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		if n < 1: return []
		if n == 1: return [0]
		elif n == 2: return [0, 1]
		
		minHeight = MAX
		heights = [MAX] * n
		degrees = [0] * n


		for edge in edges:
			degrees[edge[0]] += 1
			degrees[edge[1]] += 1
			
		for node, degree in enumerate(degrees):
			if degree == 1:
				continue
			
			height = self.getHeight(n, node, edges)
			heights[node] = height
			minHeight = min(minHeight, height)
			
		result = []
		for node, height in enumerate(heights):
			if height == minHeight:
				result.append(node)

		return result
		





class Solution2(object):
	def findMinHeightTrees(self, n, edges):
		graph = [[] for i in range(n)]
		for v1, v2 in edges:
			graph[v1].append(v2)
			graph[v2].append(v1)

		p1 = self.FindLongestPath(graph, 0)
		p2 = self.FindLongestPath(graph, p1[-1])

		print (p1, p2)

		if len(p2) % 2: return [p2[len(p2)//2]]
		else:           return [p2[len(p2)//2 - 1], p2[len(p2)//2]]

	def FindLongestPath(self, graph, root):
		queue = deque([[root]])
		traversed = set([root])
		while queue:
			path = queue.pop()
			for v in graph[path[-1]]:
				if v not in traversed:
					queue.appendleft(path + [v])
					traversed.add(v)
		return path
		


		
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

Solution2().findMinHeightTrees(n, edges)