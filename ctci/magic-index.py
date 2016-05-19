"""
A magic index in an array A[0...n-1] is defined to be an index such that 
A[i] = i

Given a sorted array of distinct integers, write a method to find a magic index,
if one exists, in array A.
"""

import unittest

def magic_search(A, start, end):
	if end < start:
		return -1

	midIdx = int((start + end)/2)
	if A[midIdx] == midIdx:
		return midIdx

	left = magic_search(A, start, min(midIdx - 1, A[midIdx]))
	if left > 0:
		return left

	right = magic_search(A, max(midIdx + 1, A[midIdx]), end)
	if right > 0:
		return right


def magic_index(A):	
	return magic_search(A, 0, len(A))

class Test(unittest.TestCase):
	data = [
		([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13], 2)
	]

	def test_long_seq(self):
		for (arr, expected) in self.data:
			self.assertEqual(magic_index(arr), expected)


unittest.main()
