"""
Given a string containing just the characters '(' and ')', find the length of the longest valid 
(well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.



()()(( ()((()))
022444 02222468


NOT COMPLETED

"""

class Solution(object):
	def longestValidParentheses(self, string):
		"""
		:type string: str
		:rtype: int
		"""

		n = len(string)
		memo = [0] * n
		opened = 0
		longest = 0

		for i in range(n):
			if string[i] == '(':
				opened += 1

			else:
				if opened > 0:
					memo[i] = 2 + memo[i - 1]
					opened -= 1
					
					# Check boundaries and check if before this sequence there was a valid input
					if i - memo[i] >= 0 and memo[i - memo[i]] > 0:
						memo[i] += memo[i - memo[i]]

					longest = max(longest, memo[i])

		return longest
		

Solution().longestValidParentheses("()()()((()))")