"""

Given an array of integers and an integer k, find out whether there are two 
distinct indices i and j in the array such that nums[i] = nums[j] and the 
difference between i and j is at most k.

"""
import unittest

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        memo = {}
        for i in range(n):
            num = nums[i]
            if num in memo and i - memo[num] <= k:
                return True
            else:
                memo[num] = i
        return False


class Test(unittest.TestCase):
    data = [
        ([1,2,3,4,6,22,55,44,77,12,25,4849,345,1231,5474,123,64,978,22], 100, True),
        ([1,0,1,1], 1, True),
        ([1], 1, False)
    ]
    def test_duplicates(self):
        for (arr, k, expected) in self.data:
            res = Solution().containsNearbyDuplicate(arr, k)
            self.assertEqual(res, expected)


unittest.main()