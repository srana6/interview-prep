"""
One Way:
There are three types of edits that can be performed on strings:

a. Insert a character
b. Remove a character
c. Replace a character

Given two strings, write a function to check if they are one edit (or zero edits) away
"""

import unittest

def _editReplace(first, second):
	editAway = False
	for i in range(len(first)):
		if first[i] != second[i]:
			if editAway:
				return False
			editAway = True
	return True


def _editAddDel(first, second):
	found = False

	index1 = 0
	index2 = 0

	while index1 < len(first) and index2 < len(second):
			
		if first[index1] != second[index2]:
			if found:
				return False

			found = True
			index2 += 1
		else:
			index1 += 1
			index2 += 1
	return True


def one_edit_away(first, second):
	lfirst, lsecond = len(first), len(second)

	if lfirst == lsecond:
		return _editReplace(first, second)
	elif lfirst + 1 ==  lsecond:
		return _editAddDel(first, second)
	elif lfirst == lsecond + 1:
		return _editAddDel(second, first)

	return False



class Test(unittest.TestCase):
	data = [
		('pale', 'ple', True),
		('pales', 'pale', True),
		('pale', 'bale', True),
		('pale', 'bake', False)
	]
	def test_one_edit_away(self):
		for (first, second, result) in self.data:
			self.assertEqual(one_edit_away(first, second), result)


unittest.main()