"""
90 - 1.2
Given two strings, write a method to 
decide if one is a permutation of the other

Following algorithm checks if a string permutation is part of the string b
"""

def count_ocurrence(string):
	hashT = {}
	for w in string:
		if w not in hashT:
			hashT[w] = 0
		hashT[w] += 1
	return hashT

def check_permutation(a, b):
	lenA, lenB = len(a), len(b)
	if lenA == 0 or lenA > lenB:
		return False
	hashA = count_ocurrence(a)
	
	for i in range(0, (lenB - lenA) + 1 ):	
		if b[i] in hashA:
			temp = count_ocurrence(b[i:i + lenA])
			if hashA == temp:
				return True
	return False

case1 = ["abbc", "cbabadcbbabbcbabaabccbabc"]

print ('Case 1', check_permutation(case1[0], case1[1]))