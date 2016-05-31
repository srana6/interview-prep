"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures


Analysis:
	string = 'abcde'
	BCR -> O(n)

	# Sorted scenario
	O(n x log n)
	'abcde'  A[0] = 'a'  -> 'bcde'

	# Unsorted
	Use Hash table
	O(n)

	-------
	This problem relates to unique characters.
	Therefore, characters can be ASCII or Unicode.

	# Fixed Array
	Time: O(1)
	SpacE: O(1)

"""


def has_unique_characters(string):
	table = {}
	n = len(string)

	for i in range(n):
		table[string[i]] = table.get(string[i], 0) + 1
		if table[string[i]] > 1:
			return False
	return True




def has_unique_characters_ascii(string):
	n_ascii = 128
	n = len(string)

	if n > n_ascii: return False

	characters = [False] * n_ascii
	for i in range(n):
		value = ord(string[i])
		
		if characters[value]:
			return False

		characters[value] = True

	return True



has_unique_characters_ascii('abcde')