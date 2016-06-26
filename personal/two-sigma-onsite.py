import unittest


def match(pattern, string):
	if not pattern and not string: return True	

	i, j = 0, 0
	while i < len(pattern) and j < len(string) and (pattern[i] == string[j] or pattern[i] == '?'):
			i += 1
			j += 1

	if i < len(pattern):
		if pattern[i] == '*':			
			return  match(pattern[i + 1:], string[j:]) or ( j < len(string) and match(pattern[i:], string[j + 1:]) )
		else: 
			return False

	return j == len(string)




class Testing(unittest.TestCase):
	def evaluator(self, data):
		for (pattern, string, expected) in data:			
			assert match(pattern, string) == expected			

	def test_single_characters(self):
		data = [
			("*", "", True),
			("*", "a", True),
			("*", "aq", True),
			("?", "a", True),
			("?", "", False),
			("?", "ab", False),
			("a", "a", True),
			("a", "b", False),
			("a", "", False),
		]
		self.evaluator(data)

	def test_multiple_characters(self):
		data = [
			("**", "", True),
			("**", "a", True),
			("**", "ab", True),
			("**", "abc", True),
			("aa*", "", False),
			("aa*", "aa", True),
			("aa*", "aab", True),
			("aa*", "aabc", True),
			("a*a", "aa", True),
			("a*a", "", False),
			("a*a", "abb", False)
		]
		self.evaluator(data)


unittest.main()
