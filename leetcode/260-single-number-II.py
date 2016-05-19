"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 10], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

from operator import xor

class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		
		partition = 0
		for num in nums:
			partition = xor(partition, num)

		bit = partition & (-partition)
		a, b = 0, 0

		for num in nums:
			if num & bit:
				a = xor(a, num)
			else:
				b = xor(b, num)

		return [a, b]


nums = [1, 2, 1, 3, 2, 10]

Solution().singleNumber(nums)