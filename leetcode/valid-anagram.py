"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""

class Solution(object):
	def isAnagram2(self, s, t):
		hashS = {}
		hashT = {}

		for i in range(len(s)):
			if s[i] not in hashS:
				hashS[s[i]] = 0
			else:
				hashS[s[i]] += 1
			
			if t[i] not in hashT:
				hashT[t[i]] = 0
			else:
				hashT[t[i]] += 1

		return hashS == hashT

	def isAnagram(self, s, t):
		if len(s) == len(t):
			dic1, dic2 = {}, {}
			for i in range(len(s)):
				dic1[s[i]] = dic1.get(s[i], 0) + 1
				dic2[t[i]] = dic2.get(t[i], 0) + 1
			return dic1 == dic2
		return False


sol = Solution()
print (sol.isAnagram("anagram", "nagaram"))
print (sol.isAnagram("", ""))
