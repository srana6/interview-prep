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
		indexes = [0] * n
		lengths = [0] * n

		max_len = 0
		curr_len = 0
		for i in range(n):
			prev_index = 

		

Solution().longestValidParentheses("()()((()((()))")