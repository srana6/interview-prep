"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

Note: 
	Come back and practice this one again later.

"""

def max_coins(inums):
	if not inums: return 0
	nums = [1] + [num for num in inums if num] + [1]
	n = len(nums)
	memo = [[0] * n for _ in range(n)]

	return burst(memo, nums, 0, n - 1)

def burst(memo, nums, left, right):	
	if memo[left][right] > 0: return memo[left][right]
	
	for i in range(left + 1, right):
		memo[left][right] = max(memo[left][right], 
							nums[left] * nums[i] * nums[right] + burst(memo, nums, left, i)
							+ burst(memo, nums, i, right))	
	return memo[left][right]


arr = [3, 1, 5, 8]
print ( max_coins(arr) )