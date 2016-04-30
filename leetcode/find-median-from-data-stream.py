"""
Find Median from Data Stream

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

import unittest
from heapq import *

class MedianFinder(object):

	def __init__(self):
		self.left = []
		self.right = []
		self.size = 0
		self.flag = True

	def unbalanced(self):		
		if self.size > 1:
			return (-self.left[0] > self.right[0])
		return False

	def hsize(self):
		return (len(self.left), len(self.right))

	def addNum(self, num):
		self.size += 1
		sleft, sright = self.hsize()
		heappush(self.left, -num)
		sleft += 1
		if sleft - sright > 1 or self.unbalanced():
			heappush(self.right, -heappop(self.left))
			sright += 1
			sleft -= 1
		if sright - sleft > 1:
			heappush(self.left, -heappop(self.right))

	def findMedian(self):
		median = 0.0
		if self.size > 0:
			if self.size % 2 == 0:				
				median = (float(-self.left[0]) + float(self.right[0]))/2.0
			else:
				sleft, sright = self.hsize()
				if sleft > sright:
					median = -(self.left[0])
				else:
					median = self.right[0]
		return median

class Test(unittest.TestCase):
	data = [
		(True, 1),
		(False, 1),
		(True, 2),
		(False, 1.5),
		(True, 3),
		(False, 2)
	]

	def test_medianFinder(self):
		mf = MedianFinder()
		val = None
		for (op, num) in self.data:
			if op:
				mf.addNum(num)
			else:
				val = mf.findMedian()
				self.assertEqual(val, num)
unittest.main()
