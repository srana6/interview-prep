"""
Excel Column Number

Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

	A -> 1
	
	B -> 2
	
	C -> 3
	
	...
	
	Z -> 26
	
	AA -> 27
	
	AB -> 28 

"""


class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, string):
		result = 0
		n = len(string)

		for i in range(n):
			val = ord(string[i]) - ord('A') + 1
			result = result * 26 + val

		return
		



Solution().titleToNumber("AAA")