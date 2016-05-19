"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 


(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.


NOT WORKING...

"""


class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

		nums.sort()
		n = len(nums)
		print (nums)

		i = 0		
		j = n // 2

		while i <= j and i < n and j >= 0:

			# Even,   i < j
			if i % 2 == 0:
				if i + 1 < n and nums[i]

			# Odd, i > j
			else:
			if nums[i]

			i += 1



nums = [1, 5, 1, 1, 6, 4]
Solution().wiggleSort(nums)