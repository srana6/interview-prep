"""
Max Non Negative SubArray

Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]

NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length

NOTE 2: If there is still a tie, then return the segment with minimum starting index

"""

from heapq import *

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def maxset(self, array):
		if not array: return []

		subarrays = []

		n = len(array)
		i, j, total = 0, 0, 0


		while j <= n:

			# Change in subarray
			if j == n or array[j] + total < total:

				# If its a valid subarray, add to heap
				if i != j and array[i] >= 0:
					length = j - i + 1

					# Use a max heap to get the subarray with highest sum and length
					heappush(subarrays, (-total, -length, i, j))
					total = 0

				# If still traversing and next element is negative, skip
				if j < n and array[j] < 0:					
					j += 1
					i = j

				# Not negative, stay there as start of new subarray
				else:
					i = j
					j += 1

			# Valid subarray, keep increasing size
			else:
				total += array[j]
				j += 1

		if subarrays:
			# Remove max from heap
			total, length, i, j = heappop(subarrays)
			return array[i:j]
		else:
			return []


A = [ -1, -1, -1, -1, -1 ]
A = [1, 2, 5, -7, 1, 2, 5]
print ( Solution().maxset(A) )


		