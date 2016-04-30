class Island(object):

	moves = [
		[-1, -1, -1,  0, 0,  1, 1, 1], 
		[-1,  0,  1, -1, 1, -1, 0, 1]
	]

	def __init__(self, island):
		self.island = island
		self.rows = len(island)
		self.columns = len(island[0])

	def isSafe(self, visited, i, j):	
		return (i >= 0 and i < self.rows and \
				j >= 0 and j < self.columns) and \
				self.island[i][j] and \
				not visited[i][j]

	def dfs(self, visited, i, j):
		visited[i][j] = True
		for x in range(8):
			iNext = i + self.moves[0][x]
			jNext = j + self.moves[1][x]
			if 	self.isSafe(visited, iNext, jNext):
				self.dfs(visited, iNext, jNext)

	def find_islands(self):
		count = 0		
		visited = [[False for x in range(self.columns)] for y in range(self.rows)]
		for i in range(self.rows):
			for j in range(self.columns):
				if self.island[i][j] and not visited[i][j]:
					self.dfs(visited, i, j)
					count += 1
		return count







island = [  
	[1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

sol = Island(island)
print (sol.find_islands())