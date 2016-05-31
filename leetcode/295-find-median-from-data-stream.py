"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2


"""


from heapq import *

class MedianFinder:
	def __init__(self):
		self.leftside = []
		self.rightside = []

	def addNum(self, num):
		heappush(self.rightside, num)
		heappush(self.leftside, -heappop(self.rightside))

		if len(self.leftside) > len(self.rightside):
			heappush(self.rightside, -heappop(self.leftside))

	def addNum2(self, num):
		"""
		Adds a num into the data structure.
		:type num: int
		:rtype: void
		"""
		if len(self.leftside) < len(self.rightside):
			heappush(self.leftside, -num)
		else:
			heappush(self.rightside, num)

		if  self.leftside and self.rightside:
			while -self.leftside[0] > self.rightside[0]:
				elem_left = heappop(self.leftside)
				elem_right = heappop(self.rightside)

				heappush(self.rightside, -elem_left)
				heappush(self.leftside, -elem_right)

	def findMedian(self):
		"""
		Returns the median of current data stream
		:rtype: float
		"""
		median = 0.0
		if self.leftside and len(self.leftside) == len(self.rightside):
			median = (-self.leftside[0] + self.rightside[0]) / 2.0

		else:
			# left
			if self.leftside and len(self.leftside) > len(self.rightside):
				median = -self.leftside[0]

			elif self.rightside:
				median = self.rightside[0]		
		return median
		

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(2)
mf.addNum(10)
mf.addNum(8)
mf.addNum(4)
mf.findMedian()
mf.addNum(100)
mf.findMedian()