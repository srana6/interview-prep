"""
.136
Given an array of integers, every element appears 
twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
"""

from operator import xor


class Solution(object):
	def singleNumber(self, nums):
		xoring = 0
		for num in nums:
			xoring = xor(xoring, num)
		return xoring
		

test1 = [2, 2, 9, 8, 7, 9, 7, 8, 1]
test2 = [1, 9, 4, 5, 4, 9, 1]
sol = Solution()
print (sol.singleNumber(test1))
print (sol.singleNumber(test2))
