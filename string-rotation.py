"""
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call
to isSubstring 

"waterbottle" is a rotation of "erbottlewat"

"""


def isSubstring(s1, s2):	
	return s2 in s1


def isRotation(s1, s2):
	if len(s1) == len(s2): 
		match = False
		j = 0
		for i in range(len(s2)):
			if s2[i] == s1[j]:
				match = True
				j += 1
			else:
				match = False
				j = 0

		if match:
			return isSubstring(s1, s2[:len(s2) - j])
	return False

def isRotation2(s1, s2):
	ln = len(s1)
	if ln == len(s2) and ln > 0:
		s1 += s1
		return isSubstring(s1, s2)
	return False



s1 = "waterbottle"
s2 = "erbottlewat"

print (isRotation(s1, s2))
print (isRotation2(s1, s2))


