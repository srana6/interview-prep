"""
Ways to Decode
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

Example :

Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


# Initialize set
mapping = set()
for i in range(1, 27):
	mapping.add(str(i))


class Solution:
	def isValid(self, string):
		return string in mapping
	
	def ways(self, A, start, memo):
		if start == len(A): return 1
		if not self.isValid(A[start]): return 0

		if start in memo:
			return memo[start]
		
		result = 0
		# 1 digit
		result += self.ways(A, start + 1, memo)

		# 2 digit
		if start < len(A) - 1 and self.isValid(A[start] + A[start + 1]):
			result += self.ways(A, start + 2, memo)

		memo[start] = result
		return memo[start]
	
	# @param A : string
	# @return an integer
	def numDecodings(self, A):
		memo = {}		
		result = self.ways(A, 0, memo)
		return result
		
		
string = "875361268549483279131"


sol = Solution().numDecodings(string)
print (sol)