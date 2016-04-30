"""
90 - 1.1
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
"""

def unique_characters(string):
	hashT= {}
	for i in range(len(string)):
		if string[i] not in hashT:
			hashT[string[i]] = 1
		else:
			return False
	return True

case1 = "abcdefgthyiklo"
case2 = "aabvkr"
case3 = "h"
case4 = "bb"
case5 = ""

print ('Case 1', unique_characters(case1))
print ('Case 2', unique_characters(case2))
print ('Case 3', unique_characters(case3))
print ('Case 4', unique_characters(case4))
print ('Case 5', unique_characters(case5))