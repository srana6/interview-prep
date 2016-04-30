"""
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in 
the array, and it should return false if every element is distinct.

X xor X -> 0
0 xor X -> X 
"""

class Solution(object):
	def containsDuplicate(self, nums):
		hashT = {}
		for i in nums:
			if i not in hashT:
				hashT[i] = True
			else:
				return True
		return False

	def containsDuplicate_set(self, nums):
		size_nums = len(nums)
		size_dupl = len(set(nums))
		return (size_nums > size_dupl)