from heapq import *
"""
Given an numsay with n objects colored red, white or blue, sort them so that objects of the same 
color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.


INCOMPLETE
Error

"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        low = 0
        high = len(nums) - 1

        i = 0
        while i <= high:
        	while nums[i] == 2 and i < high:
        		nums[i], nums[high] = nums[high], nums[i]
        		high -= 1

        	while nums[i] == 0 and i > low:
        		nums[i], nums[low] = nums[low], nums[i]
        		low += 1
        	i += 1

        
nums = [1, 0]

Solution().sortColors(nums)

print (nums)