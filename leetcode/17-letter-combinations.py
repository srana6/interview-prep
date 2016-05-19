"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""

from collections import deque
class Solution(object):
	def __init__(self):
		self.letters = {}
		self.letters['0'] = [" "]
		self.letters['1'] = ["*"]
		self.letters['2'] = ["a", "b", "c"]
		self.letters['3'] = ["d", "e", "f"]
		self.letters['4'] = ["g", "h", "i"]
		self.letters['5'] = ["j", "k", "l"]
		self.letters['6'] = ["m", "n", "o"]
		self.letters['7'] = ["p", "q", "r", "s"]
		self.letters['8'] = ["t", "u", "v"]
		self.letters['9'] = ["w", "x", "y", "z"]
	

	def permute(self, prefix, digits):
		if not digits:
			return prefix

		digit = digits.popleft()	
		if digit not in self.letters: return []
		
		newPrefix = []
		for elem in prefix:
			for letter in self.letters[digit]:
				newPrefix.append(elem + letter)
		
		prefix = newPrefix
		return self.permute(prefix, digits)

	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits: return []
		digits = deque(digits)		
		return self.permute([""], digits)

		

Solution().letterCombinations("234")