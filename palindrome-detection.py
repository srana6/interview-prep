import unittest

"""
Determine if a string is a palindrome
"""


def palindrome_check(string):
	start = 0
	end = len(string) - 1

	# Traverse array from outside to inside checking if their elements are the same
	while start < end and string[start] == string[end]:
		start += 1
		end -= 1

	# If traversed completely, then its a palindrome
	if start >= end:
		return True

	return False



class Test(unittest.TestCase):
	def test_palindrome(self):
		data = [
			("abcdcba", True),
			("abccba", True),
			("abcdcbaooo", False)
		]

		for (string, desired) in data:
			result = palindrome_check(string)

			self.assertEqual(result, desired)

unittest.main()