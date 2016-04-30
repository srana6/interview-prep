"""
Given a string, write a function to check if it is a permutation of a palindrome
A palinfrome is a owrd or phrase that is the same forwards and backwrds.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

example:
	
	Input:  Tact Coa
	Output: True  ->   permutations: "taco cat", "atco cta", etc

Analysis:
	Is the problem case sensitive?
		-> Convert everything to lowercase

	Brute Force:
		Calculate all permutations of the string
		Verify if any of the permutations is a palindrome.

		Time:  O( n! * n) ->  O(n!)
		Space: O(n!)

	Optimize:
		BCR:  O(n)

		Traverse the array and store each character frequency.
		Every frequency shall be Even. Except a maximum of 1 with frequency 1. Which could represent an Odd case

		Use hash tables:
		Space: O(n)
		Time:  O(1)
"""

def count_frequencies(string):
	characters = [0] * 128
	for i in range(len(string)):
		if string[i] != ' ':
			value = ord(string[i])
			characters[value] += 1
	return characters

def check_max_OneOdd(table):
	max_odd = 1
	for i in range(len(table)):
		if table[i] and table[i] % 2 != 0:
			max_odd -= 1

			if max_odd < 0:
				return False
	return True

def palindrome_permutation(string):
	string = list(string.lower())
	characters = count_frequencies(string)
	return check_max_OneOdd(characters)


test_arr = "Tact Coa"

res = palindrome_permutation(test_arr)
print (res)