class Solution:

	def removeDuplicates(self, nums):
		if not nums: return 0
		size = len(nums)
		i, j = size - 2, size - 1
		
		while i >= 0 and j >= 0:
			if nums[i] == nums[j]:
				del nums[j]
				
			j -= 1
			i -= 1
		return len(nums)
		
		
		
		
A = [ 0 ]

Solution().removeDuplicates(A)

print (A)