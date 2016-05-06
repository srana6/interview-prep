import unittest

"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
	["ate", "eat","tea"],
	["nat","tan"],
	["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.

"""

class Solution(object):
	def groupAnagrams(self, strs):
		if not strs: return []

		n = len(strs)
		table = {}

		# Loop through each string
		for i, string in enumerate(strs):
			# Create 'code' to use as key for the mapping 
			code = "".join(sorted(string))

			# Store each word belong to same anagram in an array with the 'code'
			table[code] = table.get(code, [])
			table[code].append(string)

		result = []
		# move from hash table to list of lists
		for group in sorted(table.values()):
			result.append(sorted(group))
	
		return result



class Test(unittest.TestCase):
	def test_merging(self):
		data = [
			(["eat", "tea", "tan", "ate", "nat", "bat"], [['bat'], ['ate', 'eat', 'tea'], ['nat', 'tan']])
		]

		for (entry, output) in data:
			result = Solution().groupAnagrams(entry)
			self.assertEqual(result, output)

unittest.main()