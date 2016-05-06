"""

Longest Increasing Subsequence
Find the longest increasing subsequence of a given sequence / array.

In other words, find a subsequence of array in which the subsequence’s elements are in 
strictly increasing order, and in which the subsequence is as long as possible. 
This subsequence is not necessarily contiguous, or unique.
In this case, we only care about the length of the longest increasing subsequence.

Example :

Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output : 6
The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]

"""

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, numbers):
		if not numbers: return 0

		n = len(numbers)
		last = n - 1

		memo = [0] * (n + 1)
		memo[0] = 1
				
		longest = 1
		for j in range(1, n):
			memo[j] = 1

			for i in range(j):
				if numbers[i] < numbers[j]:					
					memo[j] = max(memo[j], memo[i] + 1)

			longest = max(longest, memo[j])

		return longest


numbers = [ 30, 92, 22, 48, 52, 64, 92, 50, 85, 38, 97, 15, 14, 75, 59, 46, 74, 6, 95, 67, 86, 88, 25, 49, 67, 69, 50, 99, 83, 49, 60, 6, 90, 1, 50, 41, 57, 18, 36, 5, 44, 100, 23, 33, 52, 11, 46, 49, 34, 27, 77, 57, 93, 82, 38, 95, 6, 51, 100, 32, 11, 26, 50, 3, 55, 39, 84, 54, 44, 75, 76, 51, 21, 40, 28, 50, 30, 6, 84, 58, 76, 42, 35, 49, 98, 49, 13, 101, 3, 1, 60, 48, 99, 70 ]
Solution().lis(numbers)

