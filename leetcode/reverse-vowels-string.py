"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

"""

class Solution(object):
	vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
	
	def reverseVowels(self, string):
		"""
		:type s: str
		:rtype: str
		"""
		if not string: 
			return ""
		
		strList = list(string)
		n = len(strList)
		i = 0
		j = n - 1
		
		while i < j:
			if strList[i] not in self.vowels:
				i += 1
				
			if strList[j] not in self.vowels:
				j -= 1
			
			if strList[i] in self.vowels and strList[j] in self.vowels:
				strList[i], strList[j] = strList[j], strList[i]	            
				i += 1
				j -= 1
		
		return "".join(strList)