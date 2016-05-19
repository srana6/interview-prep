"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		memo = set(nums)
		max_len = 0

		while memo:	
			value = memo.pop()
			currLength = 1

			auxValue = value
			while auxValue - 1 in memo:
				currLength += 1
				memo.remove(auxValue - 1)
				auxValue -= 1

			auxValue = value
			while auxValue + 1 in memo:
				currLength += 1
				memo.remove(auxValue + 1)
				auxValue += 1

			max_len = max(max_len, currLength)

		print(max_len)
		return max_len

nums = [0,3,7,2,5,8,4,6,0,1]
#[0, 1, 2, 3, 4, 5, 6, 7, 8]
Solution().longestConsecutive(nums)