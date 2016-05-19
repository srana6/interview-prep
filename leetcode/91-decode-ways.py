"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


class Solution(object):

	def __init__(self):
		self.letters = set()
		self.lettersCount = 26

		for i in range(1, self.lettersCount + 1):
			self.letters.add(str(i))

	def numDecodings(self, string):
		"""
		:type s: str
		:rtype: int
		"""
		if not string or string[0] == '0': return 0
		if len(string) == 1: return 1

		n = len(string)		
		memo = [0] * (n + 1)
		last = n

		memo[0] = 1
		memo[1] = 1 if string[1] in self.letters else 0

		
		for i in range(2, n + 1):
			curr = string[i - 1]
			prev = string[i - 2: i]

			if curr in self.letters:
				memo[i] += memo[i - 1]

			if prev in self.letters:
				memo[i] += memo[i - 2]


			if memo[i] == 0:
				return 0

		return memo[last]



		



Solution().numDecodings("12312")

