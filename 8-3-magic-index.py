"""
A magic index in an array A[0 ... n - 1] is defined to be an index such that
A[i] = i

Given a sorted array of distinct integers, write a method to find a magic index, 
if one exists, in array A.

Note: What if the values are not distinct ?


Analysis:
	Sample 
	A = [0, 1, 9, 10, 20, 20]


	A[0] = 0
	A[1] = 1
	A[2] = 9  x

	Brute force:
		Iterate over the whole array looking for
		A[i] = i,  as soon as I find one, return
		I'd take O(n) to lookup the whole array

	Better solution:
		Since we know the array is sorted, we can lookup
		in a faster way using a binary search.

		A = [0, 1, 9,   16,   20, 20, 50]
		     0  1  2    3      4   5   6

		We can assume that if the number we stand is greater than i,
		then there wont be a magic index in the right side. So we lookup left
		We can perform this in O(lg n) in the best case.

		The problem lies when elements are not distinct, we could have a magic
		index in one side that not fulfills the previous property,
		therefore we must search in both sides.
		But, the trick is that in good cases we can perform quickly than
		O(n), which could happen in this algorithm as well. 
"""

def magic_index(A, start = 0, end = None):
	if end is None: end = len(A) - 1
	if end < start: return -1

	midIndex = (start + end) // 2
	midValue = A[midIndex]

	if midIndex == midValue:
		return midIndex
	else:
		leftIndex = min(midIndex - 1, midValue)
		left = _magic_index(A, start, leftIndex)
		if left >= 0: return left		

		rightIndex = max(midIndex + 1, midValue)
		right = _magic_index(A, rightIndex, end)
		if right >= 0: return right
	return -1



# Doesnt work for distinct values
def get_magic_index(A):
	if not A: return -1
	n = len(A)
	start = 0
	end = n - 1

	while start < end:
		midIndex = (start + end) // 2
		midValue = A[midIndex]

		# Found magic index
		if midValue == midIndex:
			return midIndex

		# Go left
		elif midValue > midIndex:
			end = midIndex 

		# Go right
		else:
			start = midIndex + 1
	return -1

A = [-10, -5, 2, 2, 2, 3, 4, 9, 12, 13]
sol = _magic_index(A)
print (sol)