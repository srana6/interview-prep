"""
Assume you have a method isSubstring which checks if one word is 
a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation 
of s1 using only one call to isSubstring

Example:  	waterbottle
			erbottlewat

Analysis:
	Brute Force:
		For each char in s2 start comparing s1 completly
		(rotate s1 from each char)
		Time: O(n^2)

	Better:
		Traverse s2 to find where s1 begin.
		Then call isSubstring from  beginning of s2 to this index
		Time: O(n)
		Space: O(1)

	xy  ->   yxyx
"""

def isSubstring(s1, s2):	
	return s1 == s2

def check_string_rotation(s1, s2):
	if not s1 or not s2 or len(s1) != len(s2): return False
	n = len(s1)
	i, j = 0, 0
	valid = False
	while j < n:
		if s2[j] == s1[i]:
			while j < n and s1[i] == s2[j]:
				i += 1
				j += 1

			if j < n:
				i = 0
		j += 1
	
	return isSubstring(s1[i:], s2[:i * -1])	

res = check_string_rotation("waterbottle", "erbottlyxat")
print (res)