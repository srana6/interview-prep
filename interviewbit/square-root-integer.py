"""
Binary search type

Square Root of Integer

Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3
DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY

"""

class Solution:
	def sqrt(self, num):
		if num <= 0: return 0
		if num == 1: return 1
		start = 0
		end = num // 2

		while start <= end:
			mid = (start + end) // 2
			value = pow(mid, 2)
			next_value = pow(mid + 1, 2)

			if value <= num and next_value > num:
				return mid

			elif value > num:
				end = mid - 1

			else:
				start = mid + 1
		return 0

res = Solution().sqrt(1)
print (res)

