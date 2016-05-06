from math import *

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return ("[%s, %s]" % (self.x, self.y))

	def __lt__(self, other):
		return self.x < other.x


def euclidean_distance(A, B):	
	return sqrt( (A.x - B.x)**2 + (A.y - B.y)**2 )

def bitonic_path_tour(points):
	MAX = float("inf")

	points.sort()
	n = len(points)
	last = n - 1

	path = [[None] * n for _ in range(n)]
	distance = [[MAX] * n for _ in range(n)]
	
	for j in range(n):
		distance[0][j] = euclidean_distance(points[0], points[j])

	for j in range(1, n):
		for i in range(j - 2):
			distance[i][j] = distance[i][j - 1] + euclidean_distance(points[j - 1], points[j])
			path[i][j] = j - 1
		
		distance[j - 1][j] = MAX

		for k in range(j):
			q = distance[k][j - 1] + euclidean_distance(points[k], points[j])
			if q < distance[j - 1][j]:
				distance[j - 1][j] = q
				path[j - 1][j] = k

	distance[last][last] = distance[last - 1][last] + euclidean_distance(points[last - 1], points[last])

	for row in distance:
		print (row)

	for row in path:
		print (row)

	print (points)




points = []
points.append(Point(1, 2))
points.append(Point(3, 2))
points.append(Point(-1, 4))
points.append(Point(-5, 20))

bitonic_path_tour(points)








