"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
import unittest

class Solution(object):
	def moveZeroes(self, nums):
		size = len(nums)

		pos = 0
		for i in range(size):
			if nums[i] != 0:
				aux = nums[i]				
				nums[i] = 0
				nums[pos] = aux				
				pos += 1

		return (nums)

class Test(unittest.TestCase):
	data = [
		([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
		([0, 0, 0, 1], [1, 0, 0, 0]),
		([1, 3, 0, 6, 0, 0, 1], [1, 3, 6, 1, 0, 0, 0]),
		([1, 0, 3, 5], [1, 3, 5, 0])
	]

	def test_moveZeroes(self):
		sol = Solution()
		for (arr, excepted) in self.data:
			sol.moveZeroes(arr)


unittest.main()
