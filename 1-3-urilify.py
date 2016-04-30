"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the
"true" length of the string.

Example: 	"Mr John Smith    ", 13
			"Mr%20John%20Smith"

					     Smith"

Analysis:
	Brute Force:
		Split the string
		For each element in the string, add a '%20 as separator'
		Negative: not using integer of size of string

		Time: O(n)
		Space: O(n)

	Better Solution:
		Insert separators in place. Traversing from the end of the string

		Time: O(n)
		Space: O(1)
"""

def urlfy_string(string, length):
	string = list(string)
	n = len(string)

	j = n - 1
	i = j
	while i <= j and j >= 0:
		while string[i] == ' ':
			i -= 1

		while string[i] != ' ' and i >= 0:
			string[i], string[j] = string[j], string[i]
			i -= 1
			j -= 1

		if j - 2 >= 0:
			string[j] = '0'
			string[j - 1] = '2'
			string[j - 2] = '%'
		j = j - 3
		i = j

	print (string)
	return "".join(string)


# Cleaner solution. Actually using length
def urly_alternate(string, length):
	string = list(string)
	spaceCount = 0

	for i in range(length):
		if string[i] == ' ':
			spaceCount += 1

	newLength = length + spaceCount * 2
	for i in reversed(range(length)):
		if string[i] == ' ':
			string[newLength - 1] = '0'
			string[newLength - 2] = '2'
			string[newLength - 3] = '%'
			newLength -= 3
		else:
			string[newLength - 1] = string[i]
			newLength -= 1

	print (string)
	return "".join(string)

urlfy_string(	"Mr John Smith    ", 13)
urly_alternate(	"Mr John Smith    ", 13)