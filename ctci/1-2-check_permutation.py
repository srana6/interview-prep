"""
Given two strings, write a method to decide if one is a permutation of the other

Analysis
	str_a   abcde
	str_b   edacb

	Brute Force:
		Generate all permutations of str_a and compare each of them with str_b
		O(str_a! x str_b)

	Optimization:
		Traverse str_a and store frequencies in a Hash Table
		Traverse str_b and compare these frequencies. If they are the same, both are a permutation of the other
		Time: O(n)
		Space: O(1)
"""

# Checks if str_b is a permutation of str_a
def check_permutation(str_a, str_b):
	if not str_a or not str_b or len(str_a) != len(str_b):
		return False

	characters = [0] * 128
	n = len(str_a)

	for i in range(n):
		value = ord(str_a)
		characters[value] += 1 		

	for i in range(n):
		value = ord(str_b)
		characters[value] -= 1 
		if characters[value] < 0:
			return False

	return True

str_a = 'abcdefg'
str_b = 'gfeacbd'

result = check_permutation(str_a, str_b)

print (result)


