"""
First Missing Integer

Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.

"""

class Solution:
	# @param A : list of integers
	# @return an integer
	def firstMissingPositive(self, A):
		n = len(A)
		
		i = 0
		while i < n:			
			value = A[i]

			# if value in range [1, N]
			if value > 0 and value <= n:

				# valid,  compare if its correct position it's placed by something different
				if value != A[value - 1]:
					A[i], A[value - 1] = A[value - 1], A[i]
					
					# if new value can be re positioned, stay there
					if A[i] > 0 and A[i] <= n:
						i -= 1
			i += 1

		for i in range(n):
			value = A[i]
			if value != i + 1:		
				return i + 1

		return n + 1



# Correct solution in exactly O(n)
class Solution:
	# @param A : list of integers
	# @return an integer
	def firstMissingPositive(self, A):
		j = 0
		n = len(A)
		for i in range(n):
			if A[i] <= 0:
				A[i],A[j] = A[j],A[i]
				j+=1

		print (A)

		for i in range(j,n):
			if abs(A[i])-1+j < n and A[abs(A[i])-1+j] > 0:
				A[abs(A[i])-1+j] = -A[abs(A[i])-1+j]
		
		print (A)

		for i in range(j,n):
			if A[i] > 0:
				return i-j+1
		return n - j + 1
		

arr = [-1, 6, 2, 4, 3, 10, 1]
sol = Solution().firstMissingPositive(arr)

print (sol)

		
		