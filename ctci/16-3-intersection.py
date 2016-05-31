"""
Given two straight line segments (represented as a start point and an end point).
Compute the point of intersection, if any.


	What is for two lines to intersect
		Infinite
			slope1 != slope2
			OR 
			slope1 == slope2 , intersect in one coordinate x || y

		Straight Lines
			Same as before
			AND
			intersection with line1
			AND
			intersection with line2



"""

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Line(object):
	def __init__(self, p1, p2):
		self.p1, self.p2 = self._swap(p1, p2)
		self.slope = (p2.y - p1.y) / (p2.x - p1.x)
		self.y_intercept = p2.y - self.slope * p2.x

	def _swap(self, p1, p2):
		if p1.x <= p2.x:
			return (p1, p2)
		else:
			return (p2, p1)


def isBetween(start, end, middle):
	return start <= middle and middle <= end

def isPointBetween(start, end, middle):
	return isBetween(start.x, end.x, middle.x) and isBetween(start.y, end.y, middle.y)



def intersection(line1, line2):	

	# Points parallel
	if line1.slope == line2.slope:
		if 	line1.y_intercept == line2.y_intercept and isBetween(line1.p1, line2.p1, line2.p2):			
			return line2.p1
		return None

	# Calculate intersection
	x = (line2.y_intercept - line1.y_intercept) / (line1.slope - line2.slope)
	y = x * line1.slope + line1.y_intercept
	p_intersection = Point(x, y)


	# Check if point is valid
	# Between both segments
	if isPointBetween(line1.p1, line1.p2, p_intersection) and isPointBetween(line2.p1, line2.p2, p_intersection):
		return p_intersection

	return None


line1 = Line(Point(1, 1), Point(100, 10))
line2 = Line(Point(1, 5), Point(120, 5))

inter = intersection(line1, line2)

print (inter.x, inter.y)
