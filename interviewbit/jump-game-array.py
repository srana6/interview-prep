"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return 1 ( true ).

A = [3,2,1,0,4], return 0 ( false ).

Return 0/1 for this problem
"""


class Solution:
	
	def _canJump(self, jumps, start, memo):
		if not jumps: return 0
		if memo[start]: return True

		n = len(jumps)
		last = n - 1

		if start == last:
			return 1

		for jump in range(1, jumps[start] + 1):		
			found_path = self._canJump(jumps, start + jump, memo)
			if found_path == 1:
				memo[start + jump] = True
				return 1
		return 0

	# @param A : list of integers
	# @return an integer
	def canJump_1(self, jumps):
		if not jumps: return 0
		n = len(jumps)

		memo = [False] * n
		return self._canJump(jumps, 0, memo)







	# @param A : list of integers
	# @return an integer
	def canJump(self, jumps):
		if not jumps: return 0
		n = len(jumps)
		last = n - 1
		
		minIndex = last

		for i in reversed(range(last)):			
			if i + jumps[i] >= minIndex:
				minIndex = i

		if minIndex == 0:
			return 1

		return 0

A = [1,10,0,0,4]
resp = Solution().canJump(A)
print (resp)