"""
Find Minimum in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.

"""

class Solution(object):
    def bsearch(self, nums, start, end):
        if start == end or nums[start] < nums[end]:
            return nums[start]

        mid = (start + end) // 2        
        left = self.bsearch(nums, start, mid)
        right = self.bsearch(nums, mid + 1, end)

        return min(left, right)


    def findMin(self, nums):
        return self.bsearch(nums, 0, len(nums) - 1)


nums = [10, 20, 30, 0, 1, 4, 5, 7, 8, 9]
sol = Solution().findMin(nums)
print (sol)