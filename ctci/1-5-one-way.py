"""
There are three types of edits that can be performed on strings:

Insert a character
Remove a character
Replace a character

Given two strings, write a function to check if they are one edit, or zero edits away

Example:
	A    hello
	B    hellao

Analysis:
	Brute Force:
		Compare to all possible one edit away
		Compare to all possible one removed away
		Compare to all possible one replacement

		O(n!**)

	Solution 1:
		Traverse equally until there is a mismatch in the elements
		If so, count number of characters different, start again when similar subsequence continues

		O(n^2)



"""