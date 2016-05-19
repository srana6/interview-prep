"""
Given a string, write a function to check if 
it is a permutation of a palindrome.

A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.

The palindrome does not need to be limited to just dictionary words.
"""

def _buildCharEvenFrequency(phrase):
	hash_table = {}
	letter = None
	for i in range(len(phrase)):
		letter = phrase[i]
		if letter != ' ':
			hash_table[letter] = not hash_table.get(letter, True)
	return hash_table

def _checkMaxOneOdd(hash_table):
	check = True
	for letter in hash_table:
		if not hash_table[letter]:			
			if not check:
				return check
			check = not check
	return True

def checkPerm(phrase):
	phrase = phrase.lower()
	hash_table = _buildCharEvenFrequency(phrase)
	return _checkMaxOneOdd(hash_table)



test_str = "Tact Coa"
print ( checkPerm(test_str) )
