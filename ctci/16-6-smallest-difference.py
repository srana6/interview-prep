"""
Given two arrays of integers, compute the pair of values (one value in each array)
with the smallest (non-negative) difference. Return the difference
"""

MAX = float("inf")

def find_smallest_difference(arr1, arr2):
	arr1.sort()
	arr2.sort()

	minDiff = MAX
	n = len(arr1)
	m = len(arr2)

	i, j = 0, 0
	while i < n and j < m:
		minDiff = min(minDiff, abs(arr1[i] - arr2[j]))
		
		if arr1[i] < arr2[j]:
			i += 1
		else:
			j += 1

	return minDiff


arr1 = [15, 11, 2, 1]
arr2 = [235, 127, 23, 19, 12, 4]

print (find_smallest_difference(arr1, arr2))
