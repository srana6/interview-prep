"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""
class Solution(object):

    # O(n2)
    def rotate2(self, nums, k):
        size = len(nums)        
        for i in range(k):
            aux = nums[size-1]
            for j in reversed(range(0, size - 1)):
                nums[j + 1] = nums[j]
            nums[0] = aux

    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
