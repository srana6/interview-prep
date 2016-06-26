class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, nums):
        if not nums: return None
        size = len(nums)
        result = nums[0]

        for i in range(1, size):
            num = nums[i]            
            result ^= num

        return result


arr = [1, 2, 2, 3, 1]
sol = Solution().singleNumber(arr)


print (sol)
