"""
Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

import math
from fractions import Fraction

class Solution:
	# @param A : tuple of integers
	# @return a strings

	def digits(self, number):
		if number == 0:
			return 1

		return int(math.log10(number)) + 1

	# Consider first as prefix
	def compare(self, first, second):
		nfirst = self.digits(first)
		nsecond = self.digits(second)

		if nfirst == nsecond:
			if first > second:
				return True
			else:
				return False
		else:
			strFirst = str(first)
			strSecond = str(second)

			listFirst = "%s%s" % (first, second)
			listSecond = "%s%s" % (second, first)
			
			if listFirst > listSecond:
				return True
			else:
				return False

	def largestNumber(self, numbers):
		n = len(numbers)

		array = [elem for elem in numbers]
		
		zeroes = 0
		for j in reversed(range(n)):
			if array[j] == 0:
				zeroes += 1

			for i in reversed(range(j)):
				if self.compare(array[j], array[i]):
					aux = array[j]
					array[j] = array[i]
					array[i] = aux 

		if zeroes == n:
			return 0

		return "".join([str(array[i]) for i in range(n)])
		

	def largestNumber(self, A):
		A = sorted(A, key=lambda n: Fraction(n, 10 ** len(str(n)) - 1), reverse=True)

		print (A)

		i = 0
		while i < len(A)-1:
			if A[i] != 0:
				break
			else:
				i += 1
		ret = map(lambda x: str(x), A[i:])

		print (ret)

		return ''.join(ret)




print (Solution().compare(3, 30))


A = [3, 30, 34, 5, 9]
res = Solution().largestNumber(A)
print (res)
