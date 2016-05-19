"""
Wave Array
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]

NOTE : If there are multiple answers possible, return the one thats lexicographically smallest. 
So, in example case, you will return [2, 1, 4, 3]

"""


class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):
		if not A: return []
		n = len(A)
		A.sort()

		small = 0
		large = 1

		while large < n and small < n:
			A[small], A[large] = A[large], A[small]
			small = large + 1
			large = small + 1

		return A


A = [5, 6, 2, 9, 89, 1, 23, 9, 8, 10]
Solution().wave(A)