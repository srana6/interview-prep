"""
Find where the Commit was Bad
"""

import random

def isGood(arr, revision):
	return arr[revision]

def _getPointOfFailure(arr, start, end):
	mid = (start + end) // 2
	mid_goodness = isGood(arr, mid)
	start_goodness = isGood(arr, start)
	end_goodness = isGood(arr, end)

	print (start, end)

	if start >= end: return None

	if mid_goodness:
		left = _getPointOfFailure(arr, start, mid)
		if left: return left

		right = _getPointOfFailure(arr, mid + 1, end)
		if right: return right

	else:
		if not start_goodness:
			return start

		# Search bad in left side
		if mid - 1 >= 0 and not isGood(arr, mid - 1):
			return _getPointOfFailure(arr, start, mid)
		else:
			return mid


def getPointOfFailure(arr):
	return _getPointOfFailure(arr, 0, len(arr) - 1)

arr = [True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, False]


"""
for i in range(1000):
	commit = random.choice([True, False])
	arr.append(commit)
"""

sol = getPointOfFailure(arr)
print (sol)