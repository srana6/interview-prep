"""
Write a method to replace all space in a string charith '20%'.
You may assume that the string has sufficient space at the end to hold the 
additional characters, and that you are given the "true" length of the string.

Note: If implementing in Java, please use a character array so 
that you can perform this operation in place

Sample:
Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
"""

import unittest

# O(N)

def urlify(string, length):
	result = ''
	isSpace = False
	count = 0
	for char in string:
		if count == length:
			break		
		if char == ' ' and isSpace == False:
			isSpace = True
			count += 1			
			result += '%20'
		elif char != ' ':
			isSpace = False
			count += 1
			result += char
	return result


class Test(unittest.TestCase):	
	data = [
		("Mr   John Smi    ", 11, 'Mr%20John%20Smi')]

	def test_urlify(self):
		for [test_string, length, expected] in self.data:
			actual = urlify(test_string, length)
			self.assertEqual(actual, expected)


if __name__ == '__main__':
	unittest.main()