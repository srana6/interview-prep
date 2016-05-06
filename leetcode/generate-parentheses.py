class Solution(object):
	def __init__(self):
		self.memo = set()
		self.parentheses = "()"


	def getPermutation(self, string):
		n = len(string)
		perms = []

		for i in range(n + 1):
			new_string = string[0:i] + self.parentheses + string[i:n]
			if new_string not in self.memo:
				perms.append(new_string)
				self.memo.add(new_string)

		return perms

	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		sequence = [[""]]

		for i in range(1, n + 1):
			prev_seq = sequence[i - 1]
			new_seq = []

			for string in prev_seq:
				new_seq += self.getPermutation(string)

			sequence.append(new_seq)

		return sequence[n]



Solution().generateParenthesis(3)