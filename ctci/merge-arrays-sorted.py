import unittest

"""
Merge two sorted arrays
"""

def merge_sorted(arr1, arr2):
	""" Takes two sorted arrays and returns a single sorted array """
	if not arr1 or not arr2: return None	
	n = len(arr1)
	m = len(arr2)

	merged = [None] * (n + m)
	nm = len(merged)

	left, right = 0, 0

	# Iterate over result array
	for i in range(nm):

		# Get elements from the arrays and work easier when they dont exist
		leftValue = arr1[left] if left < n else None
		rightValue = arr2[right] if right < m else None
		
		# Take from arr1. Two scenarios:  both are valid, left only exists ->  left taken
		if (leftValue is not None and rightValue is not None and leftValue < rightValue) or rightValue is None:
			merged[i] = leftValue
			left += 1

		# Take from arr2. Two scenarios: both are valid, right only exists ->  right taken
		elif (leftValue is not None and rightValue is not None and leftValue >= leftValue) or leftValue is None:
			merged[i] = rightValue
			right += 1

	return merged


class Test(unittest.TestCase):
	def test_merging(self):
		data = [
			([1, 2, 6, 9, 12, 29], [4, 5, 23, 99], [1, 2, 4, 5, 6, 9, 12, 23, 29, 99])
		]

		for (arr1, arr2, desired) in data:
			result = merge_sorted(arr1, arr2) 

			self.assertEqual(result, desired)

unittest.main()