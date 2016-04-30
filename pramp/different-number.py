"""

Getting a Different Number

Given an array arr of n unique non-negative integers, how can you most efficiently find a non-negative integer that is not in the array?

Your solution should return such an integer or null if arr contains all possible integers.
Analyze the runtime and space complexity of your solution.

"""


import unittest
import sys


def different_number(arr):
	n = len(arr)
	if n == sys.maxsize: return None

	dic = {num: True for num in arr}

	for num in range(n):
		if num not in dic:
			return num

class Test(unittest.TestCase):
	def test_different_number(self):
		data = [
			([45, 23, 11, 7, 6, 3, 2, 1, 100, 0], 4)
		]
		
		for (arr, expected) in data:
			res = different_number(arr)
			self.assertEqual(res, expected)

unittest.main()

